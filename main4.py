import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.SeqUtils import gc_fraction
import threading

class BioFetcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧬 BioFetcher Pro v2.0")
        self.root.geometry("850x950")
        
        # --- Color Palette ---
        self.bg_color = "#f4f7f6"      
        self.accent_green = "#2d6a4f"   
        self.btn_fetch = "#40916c"      
        self.btn_blast = "#e63946"      
        self.btn_save = "#1d3557"       
        self.btn_analyze = "#f4a261"    
        self.btn_translate = "#7209b7"  # Purple for Translation
        
        self.root.configure(bg=self.bg_color)

        # --- Fonts ---
        self.header_font = ("Helvetica", 20, "bold")
        self.section_font = ("Helvetica", 12, "bold")
        self.normal_font = ("Helvetica", 10)

        # --- Header ---
        tk.Label(root, text="GENE ANALYSIS DASHBOARD", font=self.header_font, 
                 fg=self.accent_green, bg=self.bg_color).pack(pady=15)

        # --- Step 1: Config ---
        self.create_section_label("STEP 1: CONFIGURATION")
        input_frame = tk.Frame(root, bg="white", padx=20, pady=10, highlightbackground=self.accent_green, highlightthickness=1)
        input_frame.pack(pady=5, padx=40, fill="x")

        tk.Label(input_frame, text="NCBI Email:", bg="white", font=self.normal_font).grid(row=0, column=0, sticky="w")
        self.email_entry = tk.Entry(input_frame, width=40, bg="#d8f3dc", relief="flat")
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)
        self.email_entry.insert(0, "researcher@example.com")

        tk.Label(input_frame, text="Accession ID:", bg="white", font=self.normal_font).grid(row=1, column=0, sticky="w")
        self.id_entry = tk.Entry(input_frame, width=40, bg="#d8f3dc", relief="flat")
        self.id_entry.grid(row=1, column=1, padx=10, pady=5)
        self.id_entry.insert(0, "NM_000518")

        # --- Step 2: Actions ---
        self.create_section_label("STEP 2: DATA & SEARCH")
        btn_frame = tk.Frame(root, bg=self.bg_color)
        btn_frame.pack(pady=10)

        self.fetch_btn = tk.Button(btn_frame, text="📥 Fetch Data", command=self.start_fetch, bg=self.btn_fetch, fg="blue", font=self.section_font, width=12)
        self.fetch_btn.pack(side="left", padx=5)

        self.blast_btn = tk.Button(btn_frame, text="🚀 BLAST Search", command=self.start_blast, bg=self.btn_blast, fg="blue", font=self.section_font, width=12, state="disabled")
        self.blast_btn.pack(side="left", padx=5)

        self.save_btn = tk.Button(btn_frame, text="💾 Save FASTA", command=self.save_to_file, bg=self.btn_save, fg="blue", font=self.section_font, width=12, state="disabled")
        self.save_btn.pack(side="left", padx=5)

        # --- Step 3: Analytics ---
        self.create_section_label("STEP 3: BIOLOGICAL ANALYSIS")
        ana_frame = tk.Frame(root, bg=self.bg_color)
        ana_frame.pack(pady=5)

        self.analyze_btn = tk.Button(ana_frame, text="📊 Composition Analysis", command=self.analyze_sequence, bg=self.btn_analyze, fg="blue", font=self.section_font, width=20, state="disabled")
        self.analyze_btn.pack(side="left", padx=5)

        self.translate_btn = tk.Button(ana_frame, text="🧬 Translate to Protein", command=self.translate_sequence, bg=self.btn_translate, fg="blue", font=self.section_font, width=20, state="disabled")
        self.translate_btn.pack(side="left", padx=5)

        # --- Step 4: Console ---
        self.create_section_label("STEP 4: OUTPUT CONSOLE")
        self.output_area = scrolledtext.ScrolledText(root, width=95, height=22, font=("Courier New", 11), bg="#1b4332", fg="#d8f3dc")
        self.output_area.pack(pady=10, padx=20)

        self.current_seq = None

    def create_section_label(self, text):
        lbl = tk.Label(self.root, text=text, font=self.section_font, fg=self.accent_green, bg=self.bg_color, anchor="w")
        lbl.pack(fill="x", padx=40, pady=(10, 2))

    def log(self, message):
        self.output_area.insert(tk.END, message + "\n")
        self.output_area.see(tk.END)

    # --- Backend Functions ---

    def start_fetch(self):
        email = self.email_entry.get()
        gene_id = self.id_entry.get()
        if "@" not in email:
            messagebox.showwarning("Email Required", "Please enter your email for NCBI access.")
            return
        self.fetch_btn.config(state="disabled", text="Fetching...")
        threading.Thread(target=self.fetch_logic, args=(email, gene_id), daemon=True).start()

    def fetch_logic(self, email, gene_id):
        try:
            Entrez.email = email
            handle = Entrez.efetch(db="nucleotide", id=gene_id, rettype="fasta", retmode="text")
            record = SeqIO.read(handle, "fasta")
            self.current_seq = record
            self.log(f"[SUCCESS] Retrieved: {record.description[:65]}...")
            self.root.after(0, self.enable_buttons)
        except Exception as e:
            self.log(f"[ERROR] {e}")
        finally:
            self.root.after(0, lambda: self.fetch_btn.config(state="normal", text="📥 Fetch Data"))

    def enable_buttons(self):
        self.save_btn.config(state="normal")
        self.blast_btn.config(state="normal")
        self.analyze_btn.config(state="normal")
        self.translate_btn.config(state="normal")

    def analyze_sequence(self):
        if not self.current_seq: return
        seq = self.current_seq.seq.upper()
        counts = {base: seq.count(base) for base in "ATCG"}
        self.log("\n" + "="*30 + "\n NUCLEOTIDE DISTRIBUTION\n" + "="*30)
        for base, count in counts.items():
            perc = (count / len(seq)) * 100
            self.log(f"{base} : {count:<8} ({perc:>5.2f}%) {'█' * int(perc//2)}")
        self.log(f"TOTAL GC CONTENT: {gc_fraction(seq)*100:.2f}%")

    def translate_sequence(self):
        if not self.current_seq: return
        try:
            # Standard translation (handles mitochondrial/other tables if specified, but default is standard)
            protein = self.current_seq.seq.translate(to_stop=True)
            self.log("\n" + "*"*30 + "\n PROTEIN TRANSLATION\n" + "*"*30)
            self.log(f"Amino Acid Sequence (Length: {len(protein)}):\n{protein}")
            self.log("*"*30)
        except Exception as e:
            self.log(f"[TRANSLATION ERROR] {e}")

    def save_to_file(self):
        if not self.current_seq: return
        path = filedialog.asksaveasfilename(defaultextension=".fasta")
        if path:
            with open(path, "w") as f:
                f.write(f">{self.current_seq.description}\n{self.current_seq.seq}")
            messagebox.showinfo("Saved", "File saved!")

    def start_blast(self):
        self.blast_btn.config(state="disabled", text="Blasting...")
        self.log("\n>>> Connecting to NCBI BLAST Server...")
        threading.Thread(target=self.blast_logic, daemon=True).start()

    def blast_logic(self):
        try:
            result_handle = NCBIWWW.qblast("blastn", "nt", self.current_seq.seq)
            blast_record = NCBIXML.read(result_handle)
            self.log(f"\n{'Top Organism Match':<55} | {'Identity'}")
            self.log("-" * 75)
            for alignment in blast_record.alignments[:5]:
                hsp = alignment.hsps[0]
                ident = (hsp.identities / hsp.align_length) * 100
                self.log(f"{alignment.title[:53]:<55} | {ident:>6.1f}%")
        except Exception as e:
            self.log(f"[BLAST ERROR] {e}")
        finally:
            self.root.after(0, lambda: self.blast_btn.config(state="normal", text="🚀 BLAST Search"))

if __name__ == "__main__":
    root = tk.Tk()
    app = BioFetcherApp(root)
    root.mainloop()