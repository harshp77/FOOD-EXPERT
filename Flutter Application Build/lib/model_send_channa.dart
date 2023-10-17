// ignore_for_file: deprecated_member_use

import 'dart:io';

import 'package:chaquopy/chaquopy.dart';
import 'package:flutter/material.dart';
import 'package:google_ml_kit/google_ml_kit.dart';
import 'package:image_picker/image_picker.dart';
import 'package:pythonn/model_send_arahar.dart';
import 'package:pythonn/utils/routes.dart';
import 'package:velocity_x/velocity_x.dart';

import 'outputa.dart';

class MainChooserb extends StatefulWidget {
  MainChooserb({Key? key}) : super(key: key);

  @override
  State<MainChooserb> createState() => _MainChooserbState();
}

class _MainChooserbState extends State<MainChooserb> {
  File? image;
  int count = 0;
  String? text;

  pickImage(ImageSource source) async {
    final image = await ImagePicker().pickImage(source: source);

    if (image == null) return;
    final imageTemporary = File(image.path);
    final inputImage = InputImage.fromFilePath(image.path);
    final imageLabeler = GoogleMlKit.vision.imageLabeler();
    final List<ImageLabel> labels = await imageLabeler.processImage(inputImage);
    for (ImageLabel label in labels) {
      String text = label.label;
      print(text);
      final int index = label.index;
      final double confidence = label.confidence;
      if (text == 'Pattern' ||
          text == 'Metal' ||
          text == 'Monochrome' ||
          text == 'Space') {
        setState(() {
          this.count = 1;
        });
        break;
      }
    }

    setState(
      () => this.image = imageTemporary,
    );
  }

  @override
  bool showProgress = false;
  int _currentStep = 0;
  String outputOrError = "", _error = "";
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          title: "Model Selection".text.make(),
        ),
        body: SingleChildScrollView(
          child: Column(
            children: [
              Image.asset('assests/images/angshu-purkait-UwdHrmoE0fU-unsplash (2).png'),
              const SizedBox(
                height: 25,
              ),
              "Please Follow the Steps Listed".text.xl2.bold.make(),
              const SizedBox(
                height: 35,
              ),
              Stepper(
                controlsBuilder: ((context, details) => const SizedBox(
                      height: 1,
                    )),
                steps: [
                  Step(
                    title: const Text('Choose Input Method'),
                    content: Row(children: <Widget>[
                      ElevatedButton(
                          onPressed: () async {
                            await pickImage(ImageSource.camera);
                            if (_currentStep != 2) {
                              setState(() {
                                _currentStep += 1;
                              });
                            }
                          },
                          child: const Text('Camera')),
                      const SizedBox(
                        width: 20,
                      ),
                      ElevatedButton(
                          onPressed: () async {
                            await pickImage(ImageSource.gallery);
                            if (_currentStep != 2) {
                              setState(() {
                                _currentStep += 1;
                              });
                            }
                          },
                          child: const Text('Gallery')),
                    ]),
                  ),
                  Step(
                      title: const Text('Image Verification'),
                      content: Row(children: <Widget>[
                        ElevatedButton(
                            onPressed: () {
                              if (_currentStep != 2 && count == 1) {
                                setState(() {
                                  _currentStep += 1;
                                });
                              } else {
                                showAlertDialog(context);
                                if (_currentStep != 0){setState(() {
                                  _currentStep -= 1;
                                });}
                              }
                            },
                            child: const Text('Verify !'))
                      ])),
                  Step(
                    content: Row(children: <Widget>[
                      ElevatedButton(
                          onPressed: () async {
                            setState(() {
                              showProgress = true;
                            });
                            count = 0;
                            var modelpath = "C" + image!.path.toString();
                            final _result =
                                await Chaquopy.executeCode(modelpath);
                            outputOrError = _result['textOutputOrError'] ?? '';

                            setState(() {
                              showProgress = false;
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => OutputaPage(
                                      text: outputOrError,
                                    ),
                                  ));
                            });
                          },
                          child: const Text('Predict !'))
                    ]),
                    title: const Text('Predict'),
                  ),
                ],
                onStepTapped: (int newIndex) {
                  setState(() {
                    _currentStep = newIndex;
                  });
                },
                currentStep: _currentStep,
                onStepContinue: () {
                  if (_currentStep != 2) {
                    setState(() {
                      _currentStep += 1;
                    });
                  }
                },
                onStepCancel: () {
                  if (_currentStep != 0) {
                    setState(() {
                      _currentStep -= 1;
                    });
                  }
                },
              ),
              const SizedBox(
                height: 25,
              ),
            ],
          ),
        ),
      ),
    );
  }

  void showAlertDialog(BuildContext context) {
    Widget okButton = TextButton(
      child: Text("OK"),
      onPressed: () {},
    );

    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: const Text("Verification Failed"),
      content: const Text("Pulse Not Detected in the Image"),
      actions: [
        FlatButton(
          child: const Text("Cancel"),
          onPressed: () {
            Navigator.of(context).pop();
          },
        )
      ],
    );

    // show the dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }
}
