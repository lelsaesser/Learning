# Turicreate requires Python 2.7 environment
import turicreate as tc 
import os

print "Running..."
ig02_path = '/Users/lucas/Downloads/ig02'

# load all images in random order
raw_sf = tc.image_analysis.load_images(ig02_path, recursive=True, random_order = True)

# Split file names so that we can determine what kind of image each row is
# E.g. bike_005.mask.0.png -> ['bike_005', 'mask']
info = raw_sf['path'].apply(lambda path: os.path.basename(path).split('.')[:2])

# Rename columns to 'name' and 'type'
info = info.unpack().rename({'X.0': 'name', 'X.1': 'type'})

# Add to our main SFrame
raw_sf = raw_sf.add_columns(info)

# Extract label (e.g. 'bike') from name (e.g. 'bike_003')
raw_sf['label'] = raw_sf['name'].apply(lambda name: name.split('_')[0])

# Original path no longer needed
del raw_sf['path']

# Split into images and masks
sf_images = raw_sf[raw_sf['type'] == 'image']
sf_masks = raw_sf[raw_sf['type'] == 'mask']


def mask_to_bbox_coordinates(img):
    """
    Takes a tc.Image of a mask and returns a dictionary representing bounding
    box coordinates: e.g. {'x': 100, 'y': 120, 'width': 80, 'height': 120}
    """
    import numpy as np
    mask = img.pixel_data
    if mask.max() == 0:
        return None
    # Take max along both x and y axis, and find first and last non-zero value
    x0, x1 = np.where(mask.max(0))[0][[0, -1]]
    y0, y1 = np.where(mask.max(1))[0][[0, -1]]

    return {'x': (x0 + x1) / 2, 'width': (x1 - x0),
            'y': (y0 + y1) / 2, 'height': (y1 - y0)}


# Convert masks to bounding boxes (drop masks that did not contain bounding box)
sf_masks['coordinates'] = sf_masks['image'].apply(mask_to_bbox_coordinates)

# There can be empty masks (which returns None), so let's get rid of those
sf_masks = sf_masks.dropna('coordinates')

# Combine label and coordinates into a bounding box dictionary
sf_masks = sf_masks.pack_columns(['label', 'coordinates'],
                                 new_column_name='bbox', dtype=dict)

# Combine bounding boxes of the same 'name' into lists
sf_annotations = sf_masks.groupby('name',
                                 {'annotations': tc.aggregate.CONCAT('bbox')})

# Join annotations with the images. Note, some images do not have annotations,
# but we still want to keep them in the dataset. This is why it is important to
# a LEFT join.
sf = sf_images.join(sf_annotations, on='name', how='left')

# The LEFT join fills missing matches with None, so we replace these with empty
# lists instead using fillna.
sf['annotations'] = sf['annotations'].fillna([])

# Remove unnecessary columns
del sf['type']

# Save SFrame
sf.save('ig02.sframe')

print type(sf)
print type(sf['annotations'])
print type(sf['annotations'][0])