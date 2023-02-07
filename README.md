# py-protobuf-sample

This is a ridiculously simple protobuf sample in Python

The files you will find in this repository are:

- test_protobuf.py: This is the main sample file. It contains the code a developer you may write to use protofuf.
- Person.proto: This file represents the class we want to be able to use with protobuf. In the case of this sample, the file represents a Person record (source of the structure https://protobuf.dev/getting-started/pythontutorial/). This file is going to be processed to generate the following two files.
- Person_pb2.py: This file is generated by protobuf and contains the necessary declarations for its functioning.
- Person_pb2.pyi: This file is a companion file of Person_pb2 and contains the class declarations that allow us to instantiate a Person object and manipulate its attributes in our code.

---

To produce the pb2 files, the following command needs to be executed:

```
protoc ./Person.proto --python_out=./ --pyi_out=.
```

Note the flag ```--pyi_out=.``` This flag tells the ```protoc``` compiler to generate the pyi file, allowing you to easily use the helper classes to instantiate and manipulate the Person class and its attributes.

If you have not installed the grpc toolset, you will get an error running the command above. Make sure to install it using pip with the following command:

```
pip install grpcio_tools
```

Upon running this script you should see the following:

```
Source object:
Name: Hello
ID: 123456789
Email: mail@gmail.com
Phone: [number: "7777774444"
type: MOBILE
]
Serialized string: b'\n\x05Hello\x10\x95\x9a\xef:\x1a\x0email@gmail.com"\x0e\n\n7777774444\x10\x00'
Target object:
Name: Hello
ID: 123456789
Email: mail@gmail.com
Phone: [number: "7777774444"
type: MOBILE
]
```