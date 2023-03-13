
import source.fid_score as fid

def calculate_stats(path: str, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Calculation of the statistics used by the FID: mean and sigma.
    """
    fid.calculate_stats(path, batch_size, device, dims, num_workers)



def calculate_FID(paths: list, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Calculation of the FID score.
    """
    return fid.calculate_FID(paths, batch_size, device, dims, num_workers)

def load_statistics(path: str):
    """
    Loads mean and sigma from numpy archive
    """
    return fid.load_statistics(path)

def calculate_features(path: str, batch_size=50, device='cpu', dims=2048, num_workers=1):
    """
    Save image feature vectors.
    """
    fid.calculate_features(path, batch_size, device, dims, num_workers)