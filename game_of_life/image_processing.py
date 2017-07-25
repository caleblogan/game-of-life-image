from PIL import Image


def convert_to_seed(img_path):
    """
    Loads and image and creates a seed array suitable for being passed to GameGraph
    :param img_path: the path of the image to load
    :return: a 2 dimensional list used to seed GameGraph
    """
    img = Image.open(img_path)
    img = img.resize((28, 28))
    img = img.convert('L')

    converted_data = []
    row = -1
    for i, x in enumerate(img.getdata()):
        if i % img.width == 0:
            converted_data.append([])
            row += 1
        threshold = 220
        converted_data[row].append((1 if x >= threshold else 0))
    return converted_data


if __name__ == '__main__':
    # convert_to_seed('test_img.png')
    seed_data = convert_to_seed('C:/Users/cloga_000/Pictures/giants_morse_behind_enemy_lines.jpg')
