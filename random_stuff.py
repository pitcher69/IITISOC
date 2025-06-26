import open3d as o3d
import trimesh
ply_path = r"C:\Users\ESHWAR\OneDrive\Desktop\cynaptics\iitisoc\ycbv_models\models\obj_000005.ply"
# mesh = trimesh.load(ply_path)
# mesh.show()
geometry = o3d.io.read_point_cloud(ply_path)  
print("Has vertex colors:", geometry.has_colors())

# Visualize
o3d.visualization.draw_geometries([geometry],
                                  window_name="PLY Viewer",
                                  point_show_normal=False)
