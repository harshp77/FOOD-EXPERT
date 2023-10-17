import 'dart:io';
import 'package:flutter/material.dart';

import 'package:chaquopy/chaquopy.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import 'package:pythonn/choose_page.dart';
import 'package:pythonn/model_send_arahar.dart';
import 'package:pythonn/model_send_channa.dart';
import 'package:pythonn/model_send_masoor.dart';
import 'package:pythonn/utils/routes.dart';
import 'package:velocity_x/velocity_x.dart';

import 'outputa.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}
class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        brightness: Brightness.light,
      ),
      darkTheme: ThemeData(
        brightness: Brightness.dark,
      ),
      themeMode: ThemeMode.dark, 
      debugShowCheckedModeBanner: false,
      initialRoute: MyRoutes.homeRoute,
      routes: {
        MyRoutes.homeRoute: (context) => const ChoosPage(),
        MyRoutes.mainchooseaRoute: (context) => MainChoosera(),
        MyRoutes.mainchoosebRoute: (context) => MainChooserb(),
        MyRoutes.mainchoosecRoute: (context) => MainChooserc(),
      }
    );
  }
}

