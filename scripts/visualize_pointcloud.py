import zarr
import visualizer

pointcloud_path = "/home/zyf/CS_Project/3D-Diffusion-Policy-LTH/3D-Diffusion-Policy/data/adroit_pen_expert.zarr/data/point_cloud"
# pointcloud_path = "/home/zyf/CS_Project/3D-Diffusion-Policy-LTH/3D-Diffusion-Policy/data/dexart_toilet_expert.zarr/data/point_cloud"
pointcloud = zarr.open(pointcloud_path, mode='r')

print("adroit_hammer_expert")

visualizer.visualize_pointcloud(pointcloud[999,:,:])