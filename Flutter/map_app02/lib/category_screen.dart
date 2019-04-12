import 'package:flutter/material.dart';
import 'category.dart';

final _backgroundColor = Colors.green[100];

class CategoryScreen extends StatelessWidget {
  const CategoryScreen();

  static const _categoryNames = <String>[
    'Length',
    'Area',
    'Volume',
    'Mass',
    'Time',
    'Digital Storage',
    'Energy',
    'Currency',
  ];

  static const _baseColors = <Color>[
    Colors.teal,
    Colors.orange,
    Colors.pinkAccent,
    Colors.blueAccent,
    Colors.yellow,
    Colors.greenAccent,
    Colors.purpleAccent,
    Colors.red,
  ];

  static const _categoryIcons = <IconData>[
    Icons.cake,
    Icons.home,
    Icons.add,
    Icons.person,
    Icons.android,
    Icons.apps,
    Icons.phone,
    Icons.warning,
  ];

  @override
  Widget build(BuildContext context) {
    // Create a list of the eight Categories, using the names and colors
    // from above. Use a placeholder icon, such as `Icons.cake` for each
    // Category. We'll add custom icons later.
    final categories = <Category>[];
    for(int i=0; i<_categoryNames.length; i++) {
      categories.add(Category(name: _categoryNames[i], color: _baseColors[i], iconLocation: _categoryIcons[i]));
    }

    // Create a list view of the Categories
    final listOfCategories = Container(
      color: _backgroundColor,
      padding: EdgeInsets.symmetric(horizontal: 8.0),
      child: ListView(
          children: categories
      ),
    );


    // Create an App Bar
    final appBar = AppBar(
      elevation: 0.0,
      title: Text(
        'Unit Converter',
        style: TextStyle(
          color: Colors.black,
          fontSize: 30.0,
        ),
      ),
      centerTitle: true,
      backgroundColor: _backgroundColor,
    );

    return Scaffold(
      appBar: appBar,
      body: listOfCategories,
    );
  }
}