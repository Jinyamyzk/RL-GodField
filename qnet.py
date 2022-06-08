from turtle import forward
from dezero import Model
import  dezero.functions as F
import dezero.layers as L

class Qnet(Model):
    def __init__(self):
        super().__init__()
        self.l1 = L.Linear(100) # 中間層のサイズ
        self.l2 = L.Linear(6) # 行動のサイズ(カードの種類数)
    
    def forward(self, x):
        x = F.relu(self.l1)
        x = self.l2(x)
        return x
