"""
Dillon Ramsey
FireEye Yara Rule Auto-Deployment  v.2
"""
import requests
import subprocess

vx_addr_list = []
fe_addr_list = []

def deploy(user_name, user_pass, addr, url, yara_file):
    url2 = f"https://{addr}/wsapis/2.0.0/customioc/yara/add/common?target_type=all"
    r = requests.post(url, auth=(user_name, user_pass), verify=False)
    token = r.headers['X-FeApi-Token']
    subprocess.run(['curl', '-k', f'-F filename=@{yara_file}', '-H' f'X-FEApi-Token:\
    {token}',  f'https://{addr}/wsapis/v2.0.0/customioc/yara/add/common?target_type=all'])

def main():
    user_name = input("Enter user name: ")
    user_pass = input("Enter password: ")
    yara_file = input("Enter the name of the yara file: " )

    for x in vx_addr_list:
        try:
            url = f"https://{x}/wsapis/common/v2.0.0/auth/login?"
            deploy(user_name, user_pass, x, url, yara_file)
        except:
            print("Either the host is down or the yara rule is already present")

    for x in fe_addr_list:
        try:
            url = f"https://{x}/wsapis/v2.0.0/auth/login?"
            deploy(user_name, user_pass, x, url, yara_file)
        except:
            print("Host unreachable...")

if __name__=='__main__':
    main()
