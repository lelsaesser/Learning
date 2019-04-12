import 'package:flutter/material.dart';
import 'converter_screen.dart';

class Category extends StatelessWidget {
  String name;
  Color color;
  IconData iconLocation;

  Category({Key key, this.name, this.color, this.iconLocation}) : super(key: key);

  void _navigateToConverter(BuildContext context) {
    Navigator.of(context).push(MaterialPageRoute<Null>(
      builder: (BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            elevation: 1.0,
            title: Text(
              name,
              style: Theme.of(context).textTheme.display1,
            ),
            centerTitle: true,
            backgroundColor: color,
          ),
          body: ConverterScreen(name: this.name, color: this.color),
        );
      },
    ));
  }

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: Container(
        height: 100.0,
        child: InkWell(
          borderRadius: BorderRadius.circular(50.0),
          onTap: () => _navigateToConverter(context),
          splashColor: this.color,
          highlightColor: this.color,
          child: Padding(
            padding: EdgeInsets.all(8),
            child: Row(
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.all(16),
                  child: Icon(
                    this.iconLocation,
                    size: 60.0,
                  ),
                ),
                Center(
                  child: Text(
                    this.name,
                    textAlign: TextAlign.center,
                    //style: TextStyle(fontSize: 24)
                    style: Theme.of(context).textTheme.headline,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
