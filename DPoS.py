#伪代码
'''
for round i //分成很多个round，round无限持续
   dlist_i = get N delegates sort by votes //根据投票结果选出得票率最高的N个受托人
   dlist_i = shuffle(dlist_i) //随机改变顺序
   loop //round完了，退出循环
       slot = global_time_offset / block_interval
       pos = slot % N
       if dlist_i[pos] exists in this node //delegate在这个节点
           generateBlock(keypair of dlist_i[pos]) //产生block
       else
           skip
'''
