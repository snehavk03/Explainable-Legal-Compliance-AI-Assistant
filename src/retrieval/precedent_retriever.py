from sentence_transformers import SentenceTransformer
import faiss, numpy as np
class PrecedentRetriever:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)
    def build_index(self,docs):
        self.docs=docs
        self.index.add(np.array(self.model.encode(docs)))
    def search(self,q,k=3):
        qv=self.model.encode([q])
        _,idx=self.index.search(np.array(qv),k)
        return [self.docs[i] for i in idx[0]]
if __name__=="__main__":
    r=PrecedentRetriever()
    r.build_index(["XYZ Pvt. vs Emp (2019)","ABC Corp vs Contractor (2021)"])
    print(r.search("termination"))