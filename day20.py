import regex as re
import math

def prepare_puzzle(puzzle):
    images = []
    for line in puzzle:
        if line.startswith('Tile'):
            image = set()
            tile_id = int(line[5:-1])
            y = 0
        elif line == '':
            images.append((tile_id, generate_images(image)))
        else:
            for x, c in enumerate(line):
                if c == '#':
                    image.add((x, y))
            y += 1
    images.append((tile_id, generate_images(image)))
    return images

def generate_images(image, size = 9):
    images = rotate90(image, size)
    images += [flipY(image, size) for image in images]
    return images

def rotate90(coordinates, size):
    img1, img2, img3, img4 = set(), set(), set(), set()
    for x, y in coordinates:
        img1.add((x, y))
        img2.add((size-y, x))
        img3.add((size-x, size-y))
        img4.add((y, size-x))
    return [img1, img2, img3, img4]

def flipY(coordinates, size):
    result = set()
    for x, y in coordinates:
        result.add((size-x, y))
    return result

def is_equal(set1, set2):
    for a in set1:
        if a not in set2:
            return False
    for a in set2:
        if a not in set1:
            return False
    return True

def image_match(img1, img2):
    return is_equal([y for x, y in img1 if x == 0], [y for x, y in img2 if x == 9]) or \
           is_equal([y for x, y in img1 if x == 9], [y for x, y in img2 if x == 0]) or \
           is_equal([x for x, y in img1 if y == 0], [x for x, y in img2 if y == 9]) or \
           is_equal([x for x, y in img1 if y == 9], [x for x, y in img2 if y == 0])

def get_matches(puzzle):
    matches = set()
    for i, (tile_id1, image_variants1) in enumerate(puzzle[:-1]):
        found = False
        for image1 in image_variants1:
            for tile_id2, image_variants2 in puzzle[i+1:]:
                for image2 in image_variants2:
                    if image_match(image1, image2):
                        found = True
                        matches.add((tile_id1, tile_id2))
                        break
            if found:
                break
    return matches

def solve_part1(puzzle):
    matches = get_matches(puzzle)
    return math.prod([tile_id for tile_id in [tile_id for tile_id, _ in puzzle]
                if len([1 for id1, id2 in matches if id1 == tile_id or id2 == tile_id]) == 2])

def create_full_image_ids(puzzle):
    matches = get_matches(puzzle)
    temp = {tile_id: list(set([id2 if id1 == tile_id else id1 for id1, id2 in matches
                        if id1 == tile_id or id2 == tile_id]) - {tile_id})
                            for tile_id in [tile_id for tile_id, _ in puzzle]}
    size = int(math.sqrt(len(puzzle)))
    full_image_ids = [[0 for _ in range(size)] for _ in range(size)]
    edge_tile = [tile_id for tile_id, l in temp.items() if len(l) == 2][0]
    full_image_ids[0][0] = edge_tile
    full_image_ids[1][0] = temp[edge_tile][0]
    full_image_ids[0][1] = temp[edge_tile][1]
    del temp[edge_tile]
    x = 2
    while x < size:
        full_image_ids[0][x] = [tile_id for tile_id, l in temp.items() if full_image_ids[0][x-1] in l and full_image_ids[0][x-2] != tile_id and len(l) <= 3][0]
        x += 1
    y = 1
    while y < size:
        x = 0
        if full_image_ids[y][x] == 0:
            full_image_ids[y][x] = [tile_id for tile_id, l in temp.items() if full_image_ids[y-1][x] in l and len(l) <= 3][0]
            del temp[full_image_ids[y-1][x]]
        x += 1
        while x < size:
            full_image_ids[y][x] = [tile_id for tile_id, l in temp.items() if full_image_ids[y][x-1] in l and full_image_ids[y-1][x] in l][0]
            del temp[full_image_ids[y-1][x]]
            x += 1
        y += 1
    return full_image_ids

def solve_part2(puzzle):
    full_image_ids = create_full_image_ids(puzzle)
    size = int(math.sqrt(len(puzzle)))
    full_image = [[None for _ in range(size)] for _ in range(size)]
    # find the correct image variant for every id
    puzzle = dict(puzzle)
    for y, line in enumerate(full_image_ids):
        for x, tile_id in enumerate(line):
            if x == 0 and y == 0:
                found = False
                for image1 in puzzle[tile_id]:
                    for image2 in puzzle[full_image_ids[y][x+1]]:
                        for image3 in puzzle[full_image_ids[y+1][x]]:
                            if is_equal([ty for tx, ty in image1 if tx == 9], [ty for tx, ty in image2 if tx == 0]) and \
                               is_equal([tx for tx, ty in image1 if ty == 9], [tx for tx, ty in image3 if ty == 0]):
                                full_image[y][x] = image1
                                full_image[y][x+1] = image2
                                full_image[y+1][x] = image3
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
            elif y == 0:
                if full_image[y][x] == None:
                    for image in puzzle[tile_id]:
                        if is_equal([ty for tx, ty in full_image[y][x-1] if tx == 9], [ty for tx, ty in image if tx == 0]):
                            full_image[y][x] = image
                            break
            elif x == 0:
                if full_image[y][x] == None:
                    for image in puzzle[tile_id]:
                        if is_equal([tx for tx, ty in full_image[y-1][x] if ty == 9], [tx for tx, ty in image if ty == 0]):
                            full_image[y][x] = image
                            break
            else:
                for image in puzzle[tile_id]:
                    if is_equal([tx for tx, ty in full_image[y-1][x] if ty == 9], [tx for tx, ty in image if ty == 0]) and \
                       is_equal([ty for tx, ty in full_image[y][x-1] if tx == 9], [ty for tx, ty in image if tx == 0]):
                        full_image[y][x] = image
                        break
    # remove borders
    for ty, line in enumerate(full_image):
        for tx, img in enumerate(line):
            full_image[ty][tx] = {(x-1, y-1) for x, y in img if x > 0 and x < 9 and y > 0 and y < 9}
    # replace the #-coordinates with strings
    for y, line in enumerate(full_image):
        for x, img in enumerate(line):
            temp = [['.' for _ in range(8)] for _ in range(8)]
            for tx, ty in img:
                temp[ty][tx] = '#'
            full_image[y][x] = temp
    # create the full image as a single string
    image_string = ''
    for ty, line in enumerate(full_image):
        for y in range(8):
            for tx, img in enumerate(line):
                image_string += ''.join(img[y])
            image_string += '\n'
    # read the #-coordinates again from the full image
    image = set()
    for y, line in enumerate(image_string.split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                image.add((x, y))
    # generate the 8 variants of the full image
    images = generate_images(image, size * 8 - 1)
    # save every image as single string line
    image_strings = []
    for image in images:
        temp = [['.' for _ in range(size * 8)] for _ in range(size * 8)]
        for tx, ty in image:
            temp[ty][tx] = '#'
        image_strings.append(''.join([''.join(line) for line in temp]))
    # count the monsters with a regex pattern
    monster_padding = size * 8 - 20
    regex = re.compile('#.{1}.{??}#.{4}##.{4}##.{4}###.{??}.{1}#.{2}#.{2}#.{2}#.{2}#.{2}#'.replace('??', str(monster_padding)))
    for image_str in image_strings:
        monsters = len(regex.findall(image_str, overlapped=True))
        if monsters > 0:
            return image_str.count('#') - monsters * 15
