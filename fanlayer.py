import torch 
from torch import nn

class FanLayer(nn.Module):
    def __init__(self, input_dim, output_dim, p_ratio=0.25, activation='gelu', use_p_bias=True):
        super().__init__()
        self.output_dim = output_dim  
        assert 0 < p_ratio < 0.5
        
        self.p_ratio = p_ratio
        p_out_dim = int(output_dim * p_ratio)
        g_out_dim = output_dim - 2 * p_out_dim
        
        self.input_linear_p = nn.Linear(input_dim, p_out_dim, bias=use_p_bias)
        self.input_linear_g = nn.Linear(input_dim, g_out_dim)
        
        if isinstance(activation, str):
            self.activation = getattr(nn.functional, activation)
        else:
            self.activation = activation if activation else lambda x: x

    def forward(self, src):
        g = self.activation(self.input_linear_g(src))
        p = self.input_linear_p(src)
        output = torch.cat((torch.cos(p), torch.sin(p), g), dim=-1)
        return output