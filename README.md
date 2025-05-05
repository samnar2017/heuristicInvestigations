# Investigating Cryptocurrency Transfers for Forensic Accounting Purposes

Introduction:

This is an overview of the necessity for forensic analysis in the realm of digital currencies to combat fraud, tax evasion, and asset concealment. The integration of cryptocurrencies into the financial ecosystem has introduced both innovations in transactional technology and new avenues for financial misconduct. As cryptocurrencies gain acceptance in everyday transactions, the need for specialized forensic techniques to detect and investigate financial crimes involving digital currencies becomes increasingly critical. This paper delves into the methodologies applied in forensic accounting for cryptocurrencies, with a focus on combating fraud, tax evasion, and uncovering hidden assets during legal disputes such as divorce proceedings.

Objective:
To outline the methodologies and tools employed in the forensic investigation of cryptocurrency transfers.
To highlight how these investigations can support legal processes including divorce settlements and tax compliance. The objective of this document is to provide a comprehensive overview of the tools and methodologies used in the forensic investigation of cryptocurrency transactions. It also aims to highlight the role of these investigations in supporting legal processes, including compliance with tax laws and equitable asset distribution in divorce cases.

Cryptocurrency and Forensic Accounting:

Definition of Key Terms:

Cryptocurrency: Defined as digital or virtual currency that uses cryptography for security. The decentralized nature of most cryptocurrencies means that they operate without the need for a central authority, such as a bank or government.
Forensic Accounting: Involves the application of accounting expertise to track and analyze financial information meticulously, primarily for auditing and legal purposes. In the context of cryptocurrencies, forensic accounting focuses on tracing digital transactions to reveal illicit activities and to prepare financial analyses for court use.

Challenges in Cryptocurrency Investigations:

Cryptocurrency transactions pose unique challenges due to their inherent design features:

Anonymity and Pseudonymity: Unlike traditional bank transactions, cryptocurrency transactions do not inherently carry personal information. Users are identified by addresses, which are random strings of characters.
Decentralization: Cryptocurrencies operate on a global network of computers using blockchain technology which complicates the jurisdictional scope of any investigation.
Mixing Services and Change Addresses: Techniques such as using mixing services to obfuscate the transaction trail and the generation of multiple change addresses further complicate the traceability of funds.

Methodology:


1.Transaction Analysis:

Tracing Tools: Usage of blockchain analysis tools like Chainalysis, Elliptic, or CipherTrace that provide the capability to trace the flow of funds across the blockchain and identify connections between wallets can be costly especially for smaller entities or individual investigators.

Change Address Identification: Techniques to detect and link change addresses back to the originator, which are critical in understanding the full scope of transactions is possible programmatically by utilizing the Dragonglass, explore.lworks.io or hashscan.io. 

2.Pattern Recognition:
Behavioral Analysis: Detecting patterns that may indicate the use of mixing services or strategic behaviors designed to disguise the true nature of the financial activity.
Algorithmic Surveillance: Employing machine learning algorithms to identify anomalies and potential illegal activities based on transaction patterns.

3.Integration with Legal Frameworks:
Legal Collaboration: Working closely with legal experts to ensure the findings are interpretable and useful in the legal context, including understanding the nuances of laws applicable in various jurisdictions.
Evidence Handling: Ensuring that digital evidence is collected, handled, and presented in compliance with legal standards to uphold its admissibility in court.



Case Studies:

A detailed examination of specific instances where cryptocurrency forensic accounting was instrumental in resolving complex cases:
 
Divorce Proceedings: Case study on the use of forensic techniques to uncover hidden cryptocurrency assets during asset division negotiations.

In this case study we shall examine the following transaction to check if the assets were liquidated or dissimulated. 



Source dragonglass.me
The conversion between t? (tinybars) and hbar (Hedera Hashgraph's native cryptocurrency) is straightforward: 1 hbar equals 100,000,000 tinybars. To find out how many hbars are equivalent to 14,812,031,995,099 tinybars, you can simply divide the number of tinybars by 100,000,000:
Number of hbars=14,812,031,995,099 tinybars/100,000,000,148,120.32 hbars
Account 
0.0.xxxxx
-14,812,031,995,099
0.0.1133968
14,812,031,966,900
The investigated funds got transferred to account 0.0.1133968 with 
Memo
4257175298
And validated on the node 0.0.4. 

The presence of the memo suggests us that it is an exchange platform. The consensus timestamp occurred on Jan 20. 2025m 09:14 AM EST.  



Source explore.lworks.io/
Then this transfer was batched with other small transfers from other accounts and from broker account sent to another broker account. 




Provided the hypothetical scenario that there was no sale involved, we will have to find out if the 148,120,32 Hbar were fractioned into several other transfers from the hedera address 0.0.1155594 to other addresses. 

The challenge will be to find all combinations of small transfers from 0.0.1155594 where the total is close to a value 148,120,32 Hbar + the other 19 Hbar that has been transferred as well. 





We will have to extract all data data = { "Transaction ID": [ ], "Transfers": [ ], "Consensus Timestamp": [ ], "Status": [ ] }
 that occurred from 0.0.1155594 between a given time frame. 

Start Timestamp:Ê1/20/2025, 9:14:29 AM - When the transaction was initiated.

End Timestamp: 1/20/2025. 2:38:55 PM Ð For experimental purposes we will suppose that all small transactions to others accounts were made before that timestamp. 

We will suppose that the final transactions of the fractioned values occurred from account 0.0.1155594 to the different other accounts were final, and the user didnÕt try to add another level of complexity for the investigation. Therefore we shall exclude the positive transactions from our data.json file. 

LetÕs clean the json file: 

import json

data = {
    "Transaction ID cryptotransfer": [
        "0.0.1155594-1737401933-995061354",
        "0.0.1155594-1737401911-439924371",
        "0.0.1155594-1737401837-529534709",
        # More entries here...
    ],
    "Transfers": [
        "-14.38 ? to 0.0.8133058",
        "+3,164.01 ? to 0.0.8132940",
        "-260.76 ? to 0.0.8133022",
        # More entries here...
    ],
    "Consensus Timestamp": [
        "Jan 20, 2025, 2:38:55 PM EST",
        "Jan 20, 2025, 2:38:32 PM EST",
        "Jan 20, 2025, 2:37:18 PM EST",
        # More entries here...
    ],
}

# Function to remove entries with positive transfers
def clean_positive_transfers(data):
    new_ids = []
    new_transfers = []
    new_timestamps = []
    
    for id, transfer, timestamp in zip(data['Transaction ID cryptotransfer'], data['Transfers'], data['Consensus Timestamp']):
        if not transfer.strip().startswith('+'):
            new_ids.append(id)
            new_transfers.append(transfer)
            new_timestamps.append(timestamp)
    
    data['Transaction ID cryptotransfer'] = new_ids
    data['Transfers'] = new_transfers
    data['Consensus Timestamp'] = new_timestamps

    return data

# Clean the data
cleaned_data = clean_positive_transfers(data)

# Convert to JSON and print or save to a file
cleaned_json = json.dumps(cleaned_data, indent=4)
print(cleaned_json)

To find out how many combinations I have to find:

import json

data = {
    "Transaction ID cryptotransfer": [
        "0.0.1155594-1737401933-995061354",
        "0.0.1155594-1737401911-439924371",
        "0.0.1155594-1737401837-529534709",
        # More entries here...
    ],
    "Transfers": [
        "-14.38 ? to 0.0.8133058",
        "+3,164.01 ? to 0.0.8132940",
        "-260.76 ? to 0.0.8133022",
        # More entries here...
    ],
    "Consensus Timestamp": [
        "Jan 20, 2025, 2:38:55 PM EST",
        "Jan 20, 2025, 2:38:32 PM EST",
        "Jan 20, 2025, 2:37:18 PM EST",
        # More entries here...
    ],
}

# Function to remove entries with positive transfers
def clean_positive_transfers(data):
    new_ids = []
    new_transfers = []
    new_timestamps = []
    
    for id, transfer, timestamp in zip(data['Transaction ID cryptotransfer'], data['Transfers'], data['Consensus Timestamp']):
        if not transfer.strip().startswith('+'):
            new_ids.append(id)
            new_transfers.append(transfer)
            new_timestamps.append(timestamp)
    
    data['Transaction ID cryptotransfer'] = new_ids
    data['Transfers'] = new_transfers
    data['Consensus Timestamp'] = new_timestamps

    return data

# Clean the data
cleaned_data = clean_positive_transfers(data)

# Convert to JSON and print or save to a file
cleaned_json = json.dumps(cleaned_data, indent=4)
print(cleaned_json)


The array in "Transfers" has 147 values total. We assume that the user did N amount of transfers from the initial amount into different accounts. LetÕs assume N = 5, N = 4, N = 3, N = 2.  

We suppose that the total new transfers within a range of 148,100hbar and 148,139.32hbar (given that the total transfer was 148,120.32 + 10 + 9 = 148,139.32 minus transfer fees that gives us a bottom value of 148,100hbar and a top value of 148,139.32 Ð we suppose that the fees were insignificant).

To find out how many combinations we have in total: 


from math import comb

# Calculate combinations for each group size
combinations_2 = comb(147, 2)
combinations_3 = comb(147, 3)
combinations_4 = comb(147, 4)
combinations_5 = comb(147, 5)

# Calculate total combinations
total_combinations = combinations_2 + combinations_3 + combinations_4 + combinations_5

print(f"Combinations for choosing 2: {combinations_2}")
print(f"Combinations for choosing 3: {combinations_3}")
print(f"Combinations for choosing 4: {combinations_4}")
print(f"Combinations for choosing 5: {combinations_5}")
print(f"Total combinations of 2 to 5 transactions: {combinations_2} + {combinations_3} + {combinations_4} + {combinations_5} = {total_combinations}")

Combinations for choosing 2: 10731
Combinations for choosing 3: 518665
Combinations for choosing 4: 18671940
Combinations for choosing 5: 534017484
Total combinations of 2 to 5 transactions: 10731 + 518665 + 18671940 + 534017484 = 553218820


That means we will need to perform 553218820 combinations. 

I need to check also if the results of these combinations equal to one of the target values comprised within 148,100.00hbar and 148,139.32hbar. ThatÕs 3932 different values.  

Therefore the total checks we will have to perform will be equal to 553218820 combinations x 3932 target values = 2,175,256,400,240   

This approach brings us three problems: 
 Performance: This approach can be computationally expensive due to the large number of combinations and the range of target values. Consider if we need all combinations or if there's a smaller subset that would be more relevant.
 Memory Usage: Storing all combinations in memory as shown can consume a significant amount of memory for larger datasets. We may need to process combinations on the fly instead of storing them, depending on our environment.
 Scaling and Optimization: Due to the time or memory the script may consume, we might need to look into heuristic algorithms. Instead of brute-forcing through every possible combination, heuristic algorithms like genetic algorithms or simulated annealing might provide "good enough" solutions much faster.
To tailor the genetic algorithm for your specific task, we'll need to adjust both the representation of the solutions (individuals) and the fitness function to focus more effectively on the target range.
1. Representation: Ensure that individuals in your genetic algorithm population represent possible combinations of transactions effectively. This could be indices pointing to the transfers array or the actual numeric values included in the combination.
2. Fitness Function: This function should accurately reflect how close a given combination's sum is to your target range. It should prioritize solutions that are within the range and penalize those that are not.
3. Selection, Crossover, and Mutation: Properly set up these mechanisms to generate a diverse set of potential solutions but still push the population towards better and fitter individuals.
4. Termination Condition: The algorithm should stop when it either finds a satisfactory solution or after a certain number of generations to prevent infinite loops.

Downside of this approach: 
Fitness Function
The fitness function currently penalizes based on the absolute distance from the target range. This approach is generally reasonable but can be refined to encourage solutions that approach the target range more directly. We might consider a fitness function that aggressively favors values inside the target range and scales penalties based on how far outside the range a combination lies.
Running the algorithm different times 
Since genetic algorithms can converge to different local minima, running the algorithm several times can potentially yield different valid combinations. We may consider increasing the population diversity. By increasing the population size or mutation rate, the algorithm can explore more of the solution space, increasing the chance of finding different combinations.


