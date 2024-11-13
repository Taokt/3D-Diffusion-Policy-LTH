import sapien.core as sapien

engine = sapien.Engine()
renderer = sapien.SapienRenderer(default_mipmap_levels=1, offscreen_only=not False,
                                              device="cuda:0", do_not_load_texture=False)
engine.set_renderer(renderer)

print("Sapien Test Done.")