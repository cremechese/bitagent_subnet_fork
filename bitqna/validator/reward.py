# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# Copyright © 2023 RogueTensor

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import torch
from typing import List
from bitqna.validator.tasks import Task
from template.base.validator import BaseValidatorNeuron

def get_rewards(validator: BaseValidatorNeuron, task: Task, responses: List[str]) -> [torch.FloatTensor, List[str]]:
    """
    Returns a tensor of rewards for the given query and responses.

    Args:
    - task (Task): The task sent to the miner.
    - responses (List[float]): A list of responses from the miner.

    Returns:
    - torch.FloatTensor: A tensor of rewards for the given query and responses.
    - results: A list of feedback for the miner
    """
    # Get all the reward results by iteratively calling your reward() function.
    
    scores = []
    results = []
    for response in responses:
        score, task_results = task.reward(validator, response)
        scores.append(score)
        results.append(f"[bold]Task: {task.name} Results:[/bold]\n=====================\n"+"\n".join(task_results)+f"\n[bold]Total reward:[/bold] {score}")

    return [torch.FloatTensor(scores).to(validator.device), results]