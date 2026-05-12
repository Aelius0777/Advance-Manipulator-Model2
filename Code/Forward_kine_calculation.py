import numpy as np

d1 = 0.125  
a2 = 0.100  
a3 = 0.120 
def compute_dh_matrix(theta, d, a, alpha):
   
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha),  np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta),  np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0,              np.sin(alpha),               np.cos(alpha),              d],
        [0,              0,                           0,                          1]
    ])

def forward_kinematics(q1, q2, q3):
    T01 = compute_dh_matrix(theta=q1, d=d1, a=0, alpha=np.pi/2)
    T12 = compute_dh_matrix(theta=q2, d=0, a=a2, alpha=0)
    T23 = compute_dh_matrix(theta=q3, d=0, a=a3, alpha=0)
 
    T03 = T01 @ T12 @ T23
 
    x = T03[0, 3]
    y = T03[1, 3]
    z = T03[2, 3]
    
    return x, y, z

if __name__ == "__main__":
    
    target_q1 = 0.0
    target_q2 = -0.5
    target_q3 = 0.5
    
    x, y, z = forward_kinematics(target_q1, target_q2, target_q3)
    
    print(f"CEnd-Effector Coordinates:")
    print(f"X: {x:.4f} meters")
    print(f"Y: {y:.4f} meters")
    print(f"Z: {z:.4f} meters")