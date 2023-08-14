import os

def run_command(command):
    return os.system(command)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def main():
    for a in range(1, 101):
        for b in range(1, 101):
            c = gcd(a, b)
            filename = f"../script/{a}_{b}_{c}.btcsp"
            result_filename = f"/home/hps/PycharmProjects/Languages-and-Tool-Support-for-Model-Checking-of-Behavior-Trees./实验/behaverify/gcd/result/{a}_{b}_{c}.result"
            command = f"mono /home/hps/CLionProjects/BTVerifier/C#_bt/PAT.GUI2/bin/Debug/PAT3.Console.exe -btcsp {filename} {result_filename}"
            print(f"Running command: {command}")
            status = run_command(command)
            if status == 0:
                print(f"Command executed successfully: {command}")
            else:
                print(f"Error while executing command: {command}")

if __name__ == "__main__":
    main()



