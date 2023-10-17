import 'package:flutter/material.dart';
import 'package:pythonn/model_send_arahar.dart';
import 'package:pythonn/utils/routes.dart';
import 'package:velocity_x/velocity_x.dart';

class ChoosPage extends StatelessWidget {
  const ChoosPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          title: "Model Selection".text.make(),
        ),
        body: SingleChildScrollView(
          child: Column(
            children: [
              Image.asset('assests/images/yellow-green-red-lentils-brown-bowls-close-up.png'),
              const SizedBox(
                height: 25,
              ),
              "Please Choose the Category of Daal".text.xl2.bold.make(),
              const SizedBox(
                height: 35,
              ),
              ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(context, MyRoutes.mainchooseaRoute);
                      },
                      child: "Arahar".text.make())
                  .wh(130, 50),
              const SizedBox(
                height: 25,
              ),
              ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(context, MyRoutes.mainchoosebRoute);
                      },
                      child: "Channa".text.make())
                  .wh(130, 50),
              const SizedBox(
                height: 25,
              ),
              ElevatedButton(
                      onPressed: () {
                        Navigator.pushNamed(context, MyRoutes.mainchoosecRoute);
                      },
                      child: "Masoor".text.make())
                  .wh(130, 50),
              const SizedBox(
                height: 25,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
