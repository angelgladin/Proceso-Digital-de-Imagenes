.PHONY: all install_deps prepare_env clean run_compressor run_image_indexer run_filter

all:
	@echo "make install_deps"
	@echo "    Instala las bibliotecas de Python que serán usadas con pip3"
	@echo "make prepare_env"
	@echo "    Prepara el entorno creando las carpetas que serán usadas."
	@echo "make clean"
	@echo "    Limpia y elimina los archivos generados por el proyecto."
	@echo "make run_compressor IMAGES_PATH="
	@echo "    Comprime la galeria de imágenes a usar"
	@echo "make run_image_indexer"
	@echo "    Crea un archivo .idx indexando el promedio de cada imagen"
	@echo "make run_filter IMG_PATH="
	@echo "    Genera un HTML aplicando el filtro foto morsaico"

install_deps:
	@if ! [ -x "$(command -v pip3)" ] 2> /dev/null ; then \
		apt update; \
		apt install python3-pip -y ; \
	fi
	@pip3 install -r requirements.txt

prepare_env:
	@mkdir -p input/images
	@mkdir -p tmp/imgs
	@mkdir output

clean:
	@rm -rf src/__pycache__ 2> /dev/null || true
	@rm -rf tmp 2> /dev/null || true
	@rm -rf output 2> /dev/null || true
	@rm -rf input 2> /dev/null || true

run_compressor:
	@cd src && python3 image_compressor.py3 --dir ../${IMAGES_PATH}

run_image_indexer:
	@cd src && python3 image_indexer.py3 --dir ../tmp/imgs

run_filter:
	@cd src && python3 foto_morsaico.py3 --img ../${IMG_PATH} --idx ../tmp/img_averages.idx
