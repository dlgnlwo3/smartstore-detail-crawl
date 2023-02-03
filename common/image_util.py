import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PIL import Image, ImageFilter, ImageOps
import os
from pathlib import Path
from rembg import remove

# from backgroundremover import bg


def get_resize_height(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    return new_height


def get_resize_width(image, new_height):
    width, height = image.size
    ratio = width / height
    new_width = int(ratio * new_height)
    return new_width


def get_resize_width_ratio(image, new_height):
    width, height = image.size
    ratio = width / height
    new_width = int(ratio * new_height)
    return new_width, ratio


def convert_jpg_to_png(input_path: str, output_path: str):
    im = Image.open(input_path)
    im.save(output_path)


def remove_bg(input_path: str, output_path: str):
    im1 = Image.open(input_path)
    input_png = input_path.replace(".jpg", ".png")
    input_png = input_path.replace(".jpeg", ".png")
    im1.save(input_png)
    input = Image.open(input_png)
    output = remove(input)
    output.save(output_path)

    if os.path.isfile(input_png) and input_png != input_path:
        os.remove(input_png)


def remove_bg2(input_png: str, output_path: str):
    input = Image.open(input_png)
    output = remove(input)
    output.save(output_path)


# 이미지 자르기
def image_crop(input_path, output_path):
    im = Image.open(input_path)
    cropImage = im.crop((50, 50, 100, 100))
    cropImage.save(output_path)


# 이미지 사이즈 변경
def image_resize(input_path, output_path, width, height):
    im = Image.open(input_path)
    img2 = im.resize((width, height))
    img2.save(output_path)


# 이미지 필터 적용
def image_filter(input_path, output_path):
    im = Image.open(input_path)
    blurImage = im.filter(ImageFilter.BLUR)
    blurImage.save(output_path)


# 이미지 속성 확인
def image_detail(input_path):
    img = Image.open(input_path)
    print(f"이미지 파일 이름 : {img.filename}")
    print(f"이미지 파일형식(format) : {img.format}")
    print(f"이미지 용량(size) : {img.size}")
    print(f"이미지 색상모드 : {img.mode}")
    print(f"이미지 width : {img.width}")
    print(f"이미지 height : {img.height}")


# 이미지 테두리 설정
def image_border(input, output, background_color, border_thick):
    old_im = Image.open(input)
    old_size = old_im.size
    offset = int(border_thick / 2)
    new_size = (old_size[0] + border_thick, old_size[1] + border_thick)
    # background_color = "blue"  # white, black, blue, red, ...
    new_image = Image.new("RGBA", new_size, background_color)
    new_image.paste(old_im, (offset, offset))
    new_image.save(output)


def get_image_files_in_folder(folder_path, possible_img_extension):

    img_path_list = []
    # possible_img_extension = ['.jpg', '.jpeg', '.JPG', '.bmp', '.png'] # 이미지 확장자들
    for (root, dirs, files) in os.walk(folder_path):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    img_path: str = root + "/" + file_name
                    # 경로에서 \를 모두 /로 바꿔줘야함
                    img_path = img_path.replace("\\", "/")  # \는 \\로 나타내야함
                    img_path_list.append(img_path)

    return img_path_list


# if __name__ == "__main__":
#     input_path = "1.png"
#     output_path = "crop_result.png"

#     try:
#         os.remove(output_path)
#     except:
#         pass

#     image_detail(input_path)
#     background_color, border_thick = 'blue', 25
#     image_border(input_path, output_path, background_color, border_thick)

# if __name__ == "__main__":

# input_folder = os.path.join(os.getcwd(), 'images')
# output_nukkil_folder = os.path.join(os.getcwd(), 'output_nukkil')
# output_png_1000_folder = os.path.join(os.getcwd(), 'output_png_1000')
# create_folder(output_nukkil_folder)
# create_folder(output_png_1000_folder)

# image_list_not_png = get_image_files_in_folder(input_folder, possible_img_extension = ['.jpg', '.jpeg', '.JPG', '.bmp', 'png'])

# # png 변환 및 1000 * 1000 변경
# for input_path in image_list_not_png:
#     output_file = Path(input_path).stem + '.png'
#     output_path = os.path.join(output_png_1000_folder, output_file)
#     convert_jpg_to_png(input_path, output_path)
#     image_resize(output_path, output_path, 1000, 1000)

# # 누끼따기
# png_list = get_image_files_in_folder(output_png_1000_folder, possible_img_extension =['.png'])
# for png_path in png_list:
#     output_file = Path(png_path).stem + '.png'
#     output_path = os.path.join(output_nukkil_folder, output_file)
#     remove_bg(png_path, output_path)


if __name__ == "__main__":
    import urllib

    # urllib.request.urlretrieve(
    #     "https://www.costco.co.kr/medias/sys_master/images/h3c/h15/70151975239710.webp", "test.jpg"
    # )

    input = Image.open("test8.jpg")
    output = remove(input)
    output.save(f"test88.png")
    # for i in range(1, 10):
    #     val = (i * 20) + 120
    #     output = remove(input, alpha_matting=True, alpha_matting_background_threshold=val)
    #     output.save(f"test_removed2alpha_matting{val}.png")
