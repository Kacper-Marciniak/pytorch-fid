__version__ = '0.3.0'

import pytorch_fid.fid_score

def calculate_stats(path: tuple, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Calculation of the statistics used by the FID: mean and sigma.
    """
    pytorch_fid.fid_score.calculate_stats(path, batch_size, device, dims, num_workers)



def calculate_FID(paths: tuple, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Calculation of the FID score.
    """
    pytorch_fid.fid_score.calculate_FID(paths, batch_size, device, dims, num_workers)