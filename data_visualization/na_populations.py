import pygal

wm = pygal.maps.world.World()
wm.title = "Populations of Countries in North America"
wm.value_formatter = lambda num: format(num, ',')
wm.add("North America", {'us':309349000, 'ca':34126000, 'mx':113423000})
wm.render_to_file(r"C:\Users\Alvin\Desktop\Desktop\python_work\Projects\data_visualization\images\na_populations.svg")