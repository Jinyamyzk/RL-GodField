import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class QNet(nn.Module):
    def __init__(self, action_size):
        super().__init__()
        self.l1 = nn.Linear(action_size*2+3, 100) # 状態のサイズ x 中間層のサイズ
        self.l2 = nn.Linear(100, action_size) # 行動のサイズ(カードの種類数)
    
    def forward(self, x):
        x = F.relu(self.l1(x))
        x = self.l2(x)
        return x


class QLearningAgent:
    def __init__(self, action_size):
        self.gamma = 0.9
        self.lr = 0.01
        self.epsilon = 0.1
        self.action_size = action_size

        self.qnet = QNet(self.action_size)
        self.optimizer = optim.Adam(self.qnet.parameters(), lr=self.lr)

    def get_action(self, state, hand):
        if np.random.rand() < self.epsilon:
            return np.random.choice(hand)
        else:
            state = torch.tensor(state[np.newaxis, :], dtype=torch.float32)
            qs = self.qnet(state)
            mask = np.array([True if i not in hand else False for i in range(self.action_size)]) # 手札にないカードを-infにする
            mask = torch.tensor(mask[np.newaxis, :])
            qs[mask] = -float('inf')
            return qs.argmax().item()

    def update(self, state, action, reward, next_state, done):
        state = torch.tensor(state[np.newaxis, :], dtype=torch.float32)
        next_state = torch.tensor(next_state[np.newaxis, :], dtype=torch.float32)
        if done:
            next_q = np.zeros(1)  # [0.]
        else:
            next_qs = self.qnet(next_state)
            next_q = next_qs.max(1)[0]
            next_q.detach()

        target = torch.tensor(self.gamma * next_q + reward, dtype=torch.float32)
        qs = self.qnet(state)
        q = qs[:, action]

        loss_fn = nn.MSELoss()
        loss = loss_fn(q, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.data