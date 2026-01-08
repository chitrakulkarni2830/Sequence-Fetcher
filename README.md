🧬 BioFetcher Pro v2.0: Gene Analysis Dashboard
BioFetcher Pro is a high-performance Python-based desktop application designed for bioinformaticians and researchers to streamline the retrieval and analysis of genomic data. By integrating with the NCBI Entrez API and the NCBI BLAST server, it transforms raw Accession IDs into actionable biological insights.

🧪 Biochemistry Context
In a data analytics role within the life sciences, the ability to programmatically fetch and validate sequences is crucial. This tool automates the manual process of:

Sequence Acquisition: Retrieving FASTA records for specific genes (e.g., HBB for Hemoglobin).

Compositional Analysis: Calculating GC content and nucleotide distribution—key indicators of DNA stability and gene expression potential.

Proteomics Pipeline: Simulating the Central Dogma by translating nucleotide sequences into amino acid chains.

Homology Search: Utilizing BLAST (Basic Local Alignment Search Tool) to identify evolutionary relationships and species identity through sequence similarity.

🛠️ Tech Stack & Skills
Language: Python 3.x

GUI Framework: Tkinter (Custom themed)

Bioinformatics Libraries: * Biopython (Entrez, SeqIO, NCBIWWW, NCBIXML)

SeqUtils (GC fraction calculation)

Multithreading: threading module to ensure a responsive UI during heavy API calls.

API Integration: RESTful communication with NCBI databases.

🚀 Features
Real-time NCBI Fetching: Download genomic data directly using Accession IDs.

Automated BLAST Search: Perform remote sequence alignment and retrieve the Top 5 organism matches.

Nucleotide Analytics: Visualized distribution of A, T, C, and G bases with a dynamic "bar chart" in the console.

Protein Translation: Instant conversion of DNA/RNA to protein sequences (Amino Acid chains).

Data Export: Save processed records as standard .fasta files for downstream bioinformatics pipelines.

📂 Installation & Usage
1. Prerequisites
Ensure you have Python installed, then install the required dependencies:

Bash

pip install biopython
2. Run the Application
Save the script as biofetcher.py and execute:

Bash

python biofetcher.py
3. How to use:
Enter your Email (Required by NCBI for API rate limiting).

Input a Gene Accession ID (Default provided: NM_000518 for Human Hemoglobin Subunit Beta).

Click Fetch Data to initialize the record.

Use the Biological Analysis buttons to generate metrics or the BLAST Search to find homologous sequences.