#write  a program to conduct the election and 
# find the winner of an election where votes?
#A-fist enter the name of candidate 
#B-select whom to vote
Candidate1=input("enter the 1st candidate name:")
Candidate2=input("enter the 2st candidate name:")
cand1_votes=0
cand2_votes=0
voters_id=[1001,1002,1003]
no_of_voters=len(voters_id)
print("number of voters :",no_of_voters)
voted=[]
while True:
    if voters_id==[]:
        print("voting is over")
        if cand1_votes>cand2_votes:
            print(f"{candidate1} won the electio with {cand1_votes}")
        elif cand2_votes>cand1_votes:
            print(f"{candidate2} won the electio with {cand2_votes}")
        elif cand2_votes==cand1_votes:
            print("TIED")
            break
            
    else:
        voter=int(input("enter your id: "))
        if voter in voted:
            print("you are alredy voted")
        else:
            if voter in voters_id:
                print(f"1.{Candidate1}\n2.{Candidate2}")
                choice=int(input("enter your choice"))
                if choice==1:
                    cand1_voters+=1
                    print(f"you voted {Candidate1}")
                elif choice==2:
                        cand2_votes+=1
                        print(f"you voted {Candidate2}")
                        voters_id.remove(voter)
                        voted.append(voter)
            else:
                print("you are not allowed")    
