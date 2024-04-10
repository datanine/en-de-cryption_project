#使用私钥进行解密
def decrypt(pri_key,encry):             
    N,d=pri_key
    return (encry**d)%N

def main():
    pri_str = input().split(',')
    N,d = [int(x) for x in pri_str]
    pri_key = (N,d)                 #将输入的私钥转为元组
    encrypt_str = input().split(',')
    encrypt_text = [int(x) for x in encrypt_str]                #将输入的文本处理为整数
    decrypt_text = [chr(decrypt(pri_key,x)) for x in encrypt_text]            #对密文进行解密
    decrypt_show = "".join(decrypt_text)              #输出解密后的内容
    print(decrypt_show)

if __name__=='__main__':
    main()