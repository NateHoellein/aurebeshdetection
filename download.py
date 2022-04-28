from bing_image_downloader import downloader

downloader.download("trails", limit=50,  output_dir='backgrounds', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
