aarNameforCompile='gdcasdk-sign-345'
python Jenkins_Replace.py "\\bcompile\(name: \'gdcasdk.*" "./build.gradle" "compile(name: '${aarNameforCompile}', ext: 'aar')"