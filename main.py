from lynx_engine.evidence_collector import scan
from lynx_engine.identification_engine import IdentificationEngine
from lynx_engine.scoring_engine import scoreingEngine


def main():
    # path = input("Enter the path:")
    evidence = scan("~/College Projects/noir/")
    score = scoreingEngine(evidence)
    engine = IdentificationEngine(score)
    result = engine.identify()
    print("final data:")
    engine.display()

if __name__ == "__main__":
    main()