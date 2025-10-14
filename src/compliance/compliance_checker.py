class ComplianceChecker:
    def __init__(self):
        self.rules={"termination":"Section 23, Indian Contract Act","confidentiality":"IT Act 2000"}
    def check(self,t): return self.rules.get(t.lower(),"No matching law found")
if __name__=="__main__": print(ComplianceChecker().check("termination"))