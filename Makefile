ifeq ($(shell uname),Darwin)
    EXT := dylib
else
    EXT := so
endif

all: target/release/libffi_uuidv4.$(EXT)
	python main.py

target/release/libffi_uuidv4.$(EXT): src/lib.rs Cargo.toml
	cargo build --release

clean:
	rm -rf target
