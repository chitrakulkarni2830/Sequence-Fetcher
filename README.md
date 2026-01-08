# 🧬 BioFetcher Pro v2.0: Gene Analysis Dashboard

**BioFetcher Pro** is a high-performance bioinformatics desktop application designed to bridge the gap between genomic raw data and analytical insights. Built with Python, it provides a specialized GUI for researchers to retrieve, analyze, and visualize nucleotide sequences directly from the **NCBI (National Center for Biotechnology Information)** databases.



## 🧪 Project Essence: Biochemistry meets Data
In the life sciences and pharmaceutical sectors, data analytics begins with high-fidelity data acquisition. This project demonstrates a robust ETL (Extract, Transform, Load) pipeline for genomic data:
* **Extraction:** Programmatic API calls to NCBI Entrez (E-utils).
* **Transformation:** Sequence parsing, GC-content calculation, and translation of codons into amino acid chains.
* **Analysis:** Remote homology searching via the BLAST algorithm to identify evolutionary conservation and species identity.

## 🛠️ Tech Stack & Skills
* **Language:** Python 3.x
* **Libraries:** * `Biopython`: Handling complex biological file formats (FASTA) and API communication.
    * `Tkinter`: Building a responsive, multi-threaded Desktop GUI.
* **API Integration:** NCBI Entrez and NCBI BLAST (Remote server).
* **Key Concepts:** Multithreading (to ensure UI responsiveness during heavy I/O), Data Visualization, and String Manipulation.

## 🚀 Key Features
-   **Automated Fetching:** Input an Accession ID (e.g., `NM_000518` for Human Hemoglobin) to instantly retrieve the full FASTA record.
-   **Compositional Analytics:** Visualizes the distribution of Adenine, Thymine, Cytosine, and Guanine with a dynamic histogram in the console.
-   **Central Dogma Simulation:** Instant translation of DNA sequences into Protein (Amino Acid) sequences, calculating chain length and stop codon placement.
-   **Remote BLAST Search:** Executes a `blastn` search against the 'nt' database to find top organism matches and identity percentages.
-   **Data Management:** Save retrieved and processed data into standard FASTA format for use in downstream bioinformatics pipelines.


📂 Installation & Usage
Clone the repository:
git clone [https://github.com/chitrakulkarni2830/Sequence-Fetcher.git](https://github.com/chitrakulkarni2830/Sequence-Fetcher.git)

Install dependencies:
pip install biopython
