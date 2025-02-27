from torchvision.transforms import InterpolationMode  # usort: skip

from ._utils import is_simple_tensor, register_kernel  # usort: skip

from ._meta import (
    clamp_bounding_boxes,
    convert_format_bounding_boxes,
    get_dimensions_image_tensor,
    get_dimensions_image_pil,
    get_dimensions_video,
    get_dimensions,
    get_num_frames_video,
    get_num_frames,
    get_image_num_channels,
    get_num_channels_image_tensor,
    get_num_channels_image_pil,
    get_num_channels_video,
    get_num_channels,
    get_size_bounding_boxes,
    get_size_image_tensor,
    get_size_image_pil,
    get_size_mask,
    get_size_video,
    get_size,
)  # usort: skip

from ._augment import erase, erase_image_pil, erase_image_tensor, erase_video
from ._color import (
    adjust_brightness,
    adjust_brightness_image_pil,
    adjust_brightness_image_tensor,
    adjust_brightness_video,
    adjust_contrast,
    adjust_contrast_image_pil,
    adjust_contrast_image_tensor,
    adjust_contrast_video,
    adjust_gamma,
    adjust_gamma_image_pil,
    adjust_gamma_image_tensor,
    adjust_gamma_video,
    adjust_hue,
    adjust_hue_image_pil,
    adjust_hue_image_tensor,
    adjust_hue_video,
    adjust_saturation,
    adjust_saturation_image_pil,
    adjust_saturation_image_tensor,
    adjust_saturation_video,
    adjust_sharpness,
    adjust_sharpness_image_pil,
    adjust_sharpness_image_tensor,
    adjust_sharpness_video,
    autocontrast,
    autocontrast_image_pil,
    autocontrast_image_tensor,
    autocontrast_video,
    equalize,
    equalize_image_pil,
    equalize_image_tensor,
    equalize_video,
    invert,
    invert_image_pil,
    invert_image_tensor,
    invert_video,
    permute_channels,
    permute_channels_image_pil,
    permute_channels_image_tensor,
    permute_channels_video,
    posterize,
    posterize_image_pil,
    posterize_image_tensor,
    posterize_video,
    rgb_to_grayscale,
    rgb_to_grayscale_image_pil,
    rgb_to_grayscale_image_tensor,
    solarize,
    solarize_image_pil,
    solarize_image_tensor,
    solarize_video,
    to_grayscale,
)
from ._geometry import (
    affine,
    affine_bounding_boxes,
    affine_image_pil,
    affine_image_tensor,
    affine_mask,
    affine_video,
    center_crop,
    center_crop_bounding_boxes,
    center_crop_image_pil,
    center_crop_image_tensor,
    center_crop_mask,
    center_crop_video,
    crop,
    crop_bounding_boxes,
    crop_image_pil,
    crop_image_tensor,
    crop_mask,
    crop_video,
    elastic,
    elastic_bounding_boxes,
    elastic_image_pil,
    elastic_image_tensor,
    elastic_mask,
    elastic_transform,
    elastic_video,
    five_crop,
    five_crop_image_pil,
    five_crop_image_tensor,
    five_crop_video,
    hflip,  # TODO: Consider moving all pure alias definitions at the bottom of the file
    horizontal_flip,
    horizontal_flip_bounding_boxes,
    horizontal_flip_image_pil,
    horizontal_flip_image_tensor,
    horizontal_flip_mask,
    horizontal_flip_video,
    pad,
    pad_bounding_boxes,
    pad_image_pil,
    pad_image_tensor,
    pad_mask,
    pad_video,
    perspective,
    perspective_bounding_boxes,
    perspective_image_pil,
    perspective_image_tensor,
    perspective_mask,
    perspective_video,
    resize,
    resize_bounding_boxes,
    resize_image_pil,
    resize_image_tensor,
    resize_mask,
    resize_video,
    resized_crop,
    resized_crop_bounding_boxes,
    resized_crop_image_pil,
    resized_crop_image_tensor,
    resized_crop_mask,
    resized_crop_video,
    rotate,
    rotate_bounding_boxes,
    rotate_image_pil,
    rotate_image_tensor,
    rotate_mask,
    rotate_video,
    ten_crop,
    ten_crop_image_pil,
    ten_crop_image_tensor,
    ten_crop_video,
    vertical_flip,
    vertical_flip_bounding_boxes,
    vertical_flip_image_pil,
    vertical_flip_image_tensor,
    vertical_flip_mask,
    vertical_flip_video,
    vflip,
)
from ._misc import (
    convert_image_dtype,
    gaussian_blur,
    gaussian_blur_image_pil,
    gaussian_blur_image_tensor,
    gaussian_blur_video,
    normalize,
    normalize_image_tensor,
    normalize_video,
    to_dtype,
    to_dtype_image_tensor,
    to_dtype_video,
)
from ._temporal import uniform_temporal_subsample, uniform_temporal_subsample_video
from ._type_conversion import pil_to_tensor, to_image_pil, to_image_tensor, to_pil_image

from ._deprecated import get_image_size, to_tensor  # usort: skip
