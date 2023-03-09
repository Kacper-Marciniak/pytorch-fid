__version__ = '0.4.0'

import pytorch_fid.fid_score

def calculate_stats(path: str, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Calculation of the statistics used by the FID: mean and sigma.
    """
    pytorch_fid.fid_score.calculate_stats(path, batch_size, device, dims, num_workers)



def calculate_FID(paths: list, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Calculation of the FID score.
    """
    return pytorch_fid.fid_score.calculate_FID(paths, batch_size, device, dims, num_workers)

def load_statistics(path: str):
    """
    Loads mean and sigma from numpy archive
    """
    return pytorch_fid.fid_score.load_statistics(path)

def calculate_features(path: str, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Save image feature vectors.
    """
    pytorch_fid.fid_score.calculate_features(path, batch_size, device, dims, num_workers)