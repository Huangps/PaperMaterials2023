import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def update_a_and_b(a, b):
    if a >= b:
        a = a - b
    else:
        a, b = b, a
    return a, b

def generate_script(a, b):
    c = gcd(a, b)

    script = f"""
var r={a};
var q={b};
var temp =0;
var r_q_compare=0;

set_r_q_compare = [r>=q]set_r_q_compare_s{{r_q_compare=1}}->Success [] [r<q]set_r_q_compare_f{{r_q_compare=0}}->Fail ;
check_r_q_compare = [r_q_compare==1]check_r_q_compare_s->Success [] [r_q_compare==0]check_r_q_compare_f->Fail;
sub = sub_s{{r=r-q}}->Success;
store_r = store_r_s{{temp=r}}->Success;
update_r = update_r_s{{r=q}}->Success;
update_q = update_q_s{{q=temp}}->Success;

bt= (set_r_q_compare;check_r_q_compare;sub)|>(store_r;update_r;update_q);
BT = bt;Success|>Success|>>Success;

BehaviorTree1= Loop.(if(r=={c}){{BT;r_{c}->Success}}else{{BT}}); 
BehaviorTree2= Loop.(if(q==0){{BT;q_0->Success}}else{{BT}}); 
#assert BehaviorTree1 |= F r_{c};
#assert BehaviorTree2 |= G F q_0;
"""
    return script

def main():
    for a in range(1, 101):
        for b in range(1, 101):
            output_file = f"{a}_{b}_{gcd(a, b)}.btcsp"
            script_content = generate_script(a, b)

            try:
                with open(output_file, 'w') as file:
                    file.write(script_content)
                print(f"Script generated and saved to {output_file}")
            except IOError as e:
                print(f"Error while writing to {output_file}: {e}")
                sys.exit(1)

if __name__ == "__main__":
    main()
