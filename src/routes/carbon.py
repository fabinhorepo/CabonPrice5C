from flask import Blueprint, jsonify
import pandas as pd
import os

carbon_bp = Blueprint('carbon', __name__)

@carbon_bp.route('/historical-data', methods=['GET'])
def get_historical_data():
    """Retorna dados históricos de preço de carbono (2010-2020)"""
    try:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'carbon_price_uk_2010-2020_processed.csv')
        df = pd.read_csv(file_path)
        return jsonify(df.to_dict('records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@carbon_bp.route('/predictions', methods=['GET'])
def get_predictions():
    """Retorna predições de preço de carbono (2020-2030)"""
    try:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'carbon_price_uk_2020-2030_predictions.csv')
        df = pd.read_csv(file_path)
        return jsonify(df.to_dict('records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@carbon_bp.route('/combined-data', methods=['GET'])
def get_combined_data():
    """Retorna dados históricos e predições combinados"""
    try:
        # Carregar dados históricos
        historical_path = os.path.join(os.path.dirname(__file__), '..', 'carbon_price_uk_2010-2020_processed.csv')
        df_historical = pd.read_csv(historical_path)
        df_historical['type'] = 'historical'
        df_historical['price'] = df_historical['ets_price']
        
        # Carregar predições
        predictions_path = os.path.join(os.path.dirname(__file__), '..', 'carbon_price_uk_2020-2030_predictions.csv')
        df_predictions = pd.read_csv(predictions_path)
        df_predictions['type'] = 'prediction'
        df_predictions['price'] = df_predictions['predicted_ets_price']
        
        # Combinar dados
        combined = pd.concat([
            df_historical[['year', 'price', 'type']],
            df_predictions[['year', 'price', 'type']]
        ], ignore_index=True)
        
        return jsonify(combined.to_dict('records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

