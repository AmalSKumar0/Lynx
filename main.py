from lynx_engine.evidence_collector import scan
from lynx_engine.identification_engine import IdentificationEngine
from lynx_engine.scoring_engine import scoreingEngine


def main():
    # path = input("Enter the path:")
    evidence = scan("~/College Projects/noir/")
    print("Evidence from collecting engine:",evidence.display())
    score = scoreingEngine(evidence)
    print("Score from Scoring engine:",score.display())
    engine = IdentificationEngine(score)
    result = engine.identify()
    print("final data:")
    engine.display()

if __name__ == "__main__":
    main()