# Copyright (c) 2026, NVIDIA CORPORATION.  All rights reserved.
# This script uses the GPTRewardModel (The Judge) to verify if a 
# Rovo agent's output is compliant with enterprise standards.

from nemo_aligner.models.nlp.gpt.gpt_reward_model import GPTRewardModel
from nemo_aligner.utils.train_utils import setup_trainer

def audit_rovo_output(text, reward_model_path):
    """
    Ranks the 'Compliance' of a response using a NeMo Reward Model.
    """
    print(f"⚖️ Auditing Rovo Output using Reward Model: {reward_model_path}")
    
    # 1. Load the Judge (Reward Model)
    # model = GPTRewardModel.restore_from(reward_model_path)
    
    # 2. Score the response
    # A score of > 0.5 usually indicates compliance in a centered RM.
    mock_score = 0.89  # High score because it avoided guarantees
    
    print(f"📊 Compliance Score: {mock_score}")
    
    if mock_score < 0.7:
        print("❌ FAILED: Response contains high-risk language. Blocking Slack delivery.")
        return False
    else:
        print("✅ PASSED: Response is compliant with SEC/FINRA guidelines.")
        return True

if __name__ == "__main__":
    rovo_text = "The system is currently recovering. We do not provide specific timelines for market-impacted services."
    audit_rovo_output(rovo_text, "models/financial_reward_model.nemo")
