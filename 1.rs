use crate::field::FftField;
use std::rc::Rc;

#[derive(Debug, Clone)]
pub struct Radix2Group<F: FftField> {
    //这个群的大小是2的幂
    log_order: u32,       //对数:2^log_order
    omega: F,             //N次单位根
    elements: Rc<Vec<F>>, //一个列表,里面存了 $[\omega^0, \omega^1, \omega^2, \dots, \omega^{N-1}]$
}

impl<F: FftField> Radix2Group<F> {
    pub fn new(log_order: u32, ) -> Self {
        //F::ROOT_OF_UNITY是整个域最大的那个圆的生成元(假设大小是2^MAX)
        //大小是2^log_order
        let omega = F::ROOT_OF_UNITY.exp(1usize << (F::LOG_ORDER - log_order));
        //F::LOG_ORDER: 这个域支持的最大 FFT 大小的指数（比如 Goldilocks 域最大支持 $2^{32}$，这里就是 32）。
        //log_order: 你当前需要的 FFT 大小的指数（比如你要做 $2^{10}$ 的计算，这里就是 10）。
        // 差值: $32 - 10 = 22$。这意味着我们需要把原本的圆圈缩小 $2^{22}$ 倍。
        //1usize<<{..}等价于1<<22,
        //ROOT_OF_UNITY是本原单位根

        let elements = std::iter::successors(Some(F::one()), |&last| Some(last * omega))
            .take(1 << log_order)
            .collect();
        //iter::successors表示无限迭代
        //生成一个$$[1, \omega, \omega^2, \omega^3, \dots, \omega^{N-1}]$$
        //第一个数是F::one()
        //|&last Some(last*omega)|接受上一个产生的数,用上一个数*omega
        //take(1<<log_order)计算需要的总数量N,停止
        Radix2Group {
            log_order,
            omega,
            elements: Rc::new(elements),
        }
    }

    // 返回群的元素个数，即 2 的 log_order 次方
    pub fn size(&self) -> usize {
        1 << self.log_order
    }
    // 返回群中索引为 index 的元素
    pub fn element_at(&self,index:usize)->F{self.elements[index]} 
    
    //返回逆元,w^0=1,所以w^0的逆元就是1,对于其他,w^i的逆元就是w^(-i),由于w^N=1,所以w^(-i)=w^{N-i}
    pub fn element_inv_at(&self,index:usize)->F{
        if index==0{
            F::one()
        
        }
        else {
            self.elements[self.size()-index]
        }
    }

    pub fn exp(&self, index: usize) -> Radix2Group<F> {
        assert_eq!(index & (index - 1), 0);
        Radix2Group::new(self.log_order - index.ilog2())
    }
}




