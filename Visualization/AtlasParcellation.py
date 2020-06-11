from nilearn import plotting


def AtlasParcellation(path, is_probabilistic=False):
    if is_probabilistic:
        return plotting.find_probabilistic_atlas_cut_coords(maps_img=path)
    else:
        return plotting.find_parcellation_cut_coords(labels_img=path)