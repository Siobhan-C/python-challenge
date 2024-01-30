import os
import csv




input_file=os.path.join("Resources", "election_data.csv")
output_file=os.path.join("analysis", "election_analysis.txt")

total_votes=0
candidate_list=[]
candidate_dic={}
winner=["", 0]

with open(input_file) as input_data:
    reader=csv.reader(input_data)
    header=next(reader)

    for row in reader:
        total_votes=total_votes+1

        candidate=row[2]

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_dic[candidate]=0
        candidate_dic[candidate]=candidate_dic[candidate]+1


output=(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

with open(output_file,"w") as output_data:
    print(output)
    output_data.write(output)

    for x in candidate_list:
        votes=candidate_dic.get(x)
        percentage=float(votes)/float(total_votes)*100
        output=(f"{x}: {percentage:.3f}% ({votes})\n")
        print(output)
        output_data.write(output) 

        if votes > winner[1]:
            winner[1]=votes
            winner[0]=x    

    output=(
        f"-------------------------\n"
        f"Winner: {winner[0]}\n"
        f"-------------------------\n"
    )
    print(output)
    output_data.write(output) 