import 'package:flutter/material.dart';
import 'package:meta/meta.dart';

class ConverterScreen extends StatelessWidget {
  final String name;
  final Color color;

  const ConverterScreen({@required this.name, @required this.color})
      : assert(name != null),
        assert(color != null);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: color,
      margin: EdgeInsets.all(8.0),
      padding: EdgeInsets.all(16.0),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: <Widget>[
          Text(
            name,
            style: Theme.of(context).textTheme.headline,
          ),
          Text(
            "Placeholder",
            style: Theme.of(context).textTheme.subhead,
          ),
        ],
      ),
    );
  }
}