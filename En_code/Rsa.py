import math
import random

#生成小于max_num的素数
def gen_prime_num(max_num):     
    
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是素数

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_num + 1, i):
                is_prime[j] = False

    prime_num = [num for num in range(2, max_num + 1) if is_prime[num]]    

    # 试除法（trial division），检查每个数字是否能够被小于它的数整除来确定是否为素数
    # prime_num=[]
    # for i in range(2,max_num):
    #     temp=0
    #     sqrt_max_num=int(math.sqrt(i))+1
    #     for j in range(2,sqrt_max_num):
    #         if i%j==0:
    #             temp=j
    #             break
    #     if temp==0:
    #         prime_num.append(i)

    return prime_num
 
#生成公私钥
def gen_rsa_key():              
    prime=gen_prime_num(1000)
    '''
    print(prime[-80:-1])
    while 1:
        prime_str=input("\n 请从上面选择两个数字，以逗号隔开: ").split(",")
        p,q=[int(x) for x in prime_str]
        if (p in prime) and (q in prime):
            break
        else:
            print("输入错误！")
    '''
    p=random.choice(prime[-50:-1])              #从后50个素数中随机选择一个作为p
    q=random.choice(prime[-50:-1])                  #从后50个素数中随机选择一个作为q
    while(p==q):                        #如果p和q相等则重新选择
        q=random.choice(prime[-50:-1])
    N=p*q
    r=(p-1)*(q-1)
    r_prime=gen_prime_num(r)
    r_len=len(r_prime)
    e=r_prime[int(random.uniform(0,r_len))]
    d=0
    for n in range(2,r):
        if (e*n)%r==1:
            d=n
            break
    return ((N,e),(N,d))

# 将私钥公钥保存的指定位置
def write_to_file(pub_key, pri_key):
    # 打开文件以写入数据
    with open('rsa_key.txt', 'w') as file:
        # 写入数据到文件
        file.write("Public_rsa_key:\n")
        file.write(f"{pub_key}\n")
        file.write("Private_rsa_key:\n")
        file.write(f"{pri_key}\n")

#使用公钥进行加密
def encrypt(pub_key,origal):            
    N,e=pub_key
    return (origal**e)%N

def main():
    pub_key,pri_key=gen_rsa_key()
    # print(pub_key)
    # print(pri_key)
    write_to_file(pub_key, pri_key)
    
    
    plaintext=input()
    encrypt_text=[encrypt(pub_key,ord(x)) for x in plaintext]  
    encrypt_show=",".join([str(x) for x in encrypt_text])
    print(encrypt_show)

if __name__=='__main__':
    main()