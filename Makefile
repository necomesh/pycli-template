clean:
	rm -Rf ./dist/*

test:
	copier copy . ./dist

push:
	git add .
	git commit -m "release"
	git push