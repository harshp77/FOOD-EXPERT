import 'dart:io';

import 'package:flutter/material.dart';
import 'package:pythonn/utils/routes.dart';
import 'package:velocity_x/velocity_x.dart';

class OutputaPage extends StatelessWidget {
  final String text;

  // receive data from the FirstScreen as a parameter
  OutputaPage({Key? key, required this.text}) : super(key: key);
  var myfile = File('/data/user/0/com.example.pythonn/cache/imgg.png');
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: const Text('Output Screen')),
        body: Center(
          child: SingleChildScrollView(
            child: Column(children: [
              const SizedBox(
                height: 40,
              ),
              Image.file(myfile),
              const SizedBox(
                height: 40,
              ),
              Center(child: Text(text, style: const TextStyle(fontSize: 20,fontWeight: FontWeight.bold),)),
              const SizedBox(height: 30,),
              ElevatedButton(onPressed: (() => Navigator.pushNamed(context, MyRoutes.homeRoute)) , child: "Test Another Image".text.make()),
              const SizedBox(height: 40,),
              "**Quality has been determined on scale of 50-100 ".text.make(),
              "where 50 denote lowest quality and 100 denote best ".text.make()
            ]),
          ),
        ),
    );
  }
}
