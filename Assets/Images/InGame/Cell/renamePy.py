import os

for i in range(1, 7):
	os.rename(f"Tile {i}.png", f"tile-{i}.png", src_dir_fd=None, dst_dir_fd=None)