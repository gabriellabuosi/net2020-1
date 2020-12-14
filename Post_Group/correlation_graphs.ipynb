{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "correlation_graphs.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "glZUFO71MpQ1"
      },
      "source": [
        "# Import Database and Libraries"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1102
        },
        "id": "keTSCQOew2It",
        "outputId": "2be3ffc4-d3f0-4ed7-d083-007055627a49"
      },
      "source": [
        "import pandas as pd \r\n",
        "import numpy as np \r\n",
        "\r\n",
        "import statsmodels\r\n",
        "import statsmodels.api as sm\r\n",
        "import scipy.stats as stats\r\n",
        "\r\n",
        "import matplotlib.pyplot as plt\r\n",
        "\r\n",
        "# import the csv file with JUST the politicians post\r\n",
        "postDB = pd.read_csv(r\"/content/postDB.csv\", engine='python')\r\n",
        "\r\n",
        "df_post = pd.DataFrame(data=postDB)\r\n",
        "df_post"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.\n",
            "  import pandas.util.testing as tm\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>Origin_file_order</th>\n",
              "      <th>Site</th>\n",
              "      <th>p_id</th>\n",
              "      <th>dateCreated</th>\n",
              "      <th>p_politician</th>\n",
              "      <th>p_gender</th>\n",
              "      <th>p_GRUPPO_PE</th>\n",
              "      <th>p_LISTA</th>\n",
              "      <th>p_PARTITO</th>\n",
              "      <th>p_governo</th>\n",
              "      <th>p_dx_sx</th>\n",
              "      <th>p_CIRCOSCRIZIONE</th>\n",
              "      <th>p_text</th>\n",
              "      <th>p_favoriteCount</th>\n",
              "      <th>p_shareCount</th>\n",
              "      <th>p_replyCount</th>\n",
              "      <th>p_replyEval</th>\n",
              "      <th>p_numComments</th>\n",
              "      <th>p_numFakeTags</th>\n",
              "      <th>p_rating</th>\n",
              "      <th>p_category</th>\n",
              "      <th>p_topic</th>\n",
              "      <th>p_campagna</th>\n",
              "      <th>p_camapagna2</th>\n",
              "      <th>Target1</th>\n",
              "      <th>Target2</th>\n",
              "      <th>p_targe1-2</th>\n",
              "      <th>target1_s-p</th>\n",
              "      <th>target1_pol</th>\n",
              "      <th>c_text</th>\n",
              "      <th>c_level</th>\n",
              "      <th>c_replyToUser</th>\n",
              "      <th>c_replyToText</th>\n",
              "      <th>c_rating</th>\n",
              "      <th>c_rating3</th>\n",
              "      <th>c_ratingCivile</th>\n",
              "      <th>c_ratingPosNeg</th>\n",
              "      <th>c_category</th>\n",
              "      <th>Unnamed: 38</th>\n",
              "      <th>...</th>\n",
              "      <th>p_Fisico</th>\n",
              "      <th>p_Corpo</th>\n",
              "      <th>p_Sesso</th>\n",
              "      <th>p_Mangiare</th>\n",
              "      <th>p_Dormire</th>\n",
              "      <th>p_Cura_cor</th>\n",
              "      <th>p_parolac</th>\n",
              "      <th>p_Non_flu</th>\n",
              "      <th>p_riempiti</th>\n",
              "      <th>p_Voi</th>\n",
              "      <th>p_Lui_lei</th>\n",
              "      <th>p_Loro</th>\n",
              "      <th>p_Condizio</th>\n",
              "      <th>p_Transiti</th>\n",
              "      <th>p_P_pass</th>\n",
              "      <th>p_gerundio</th>\n",
              "      <th>p_Passivo</th>\n",
              "      <th>p_Essere</th>\n",
              "      <th>p_Avere</th>\n",
              "      <th>p_Formale</th>\n",
              "      <th>p_Io_Ver</th>\n",
              "      <th>p_Tu_Verbo</th>\n",
              "      <th>p_Lui_Verb</th>\n",
              "      <th>p_Noi_Verb</th>\n",
              "      <th>p_Voi_Verb</th>\n",
              "      <th>p_Loro_Ver</th>\n",
              "      <th>p_AllPunc</th>\n",
              "      <th>p_Period</th>\n",
              "      <th>p_Comma</th>\n",
              "      <th>p_Colon</th>\n",
              "      <th>p_SemiC</th>\n",
              "      <th>p_Qmark</th>\n",
              "      <th>p_Exclam</th>\n",
              "      <th>p_Dash</th>\n",
              "      <th>p_Quote</th>\n",
              "      <th>p_Apostro</th>\n",
              "      <th>p_Parenth</th>\n",
              "      <th>p_OtherP</th>\n",
              "      <th>Count</th>\n",
              "      <th>target1_2</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>30126</td>\n",
              "      <td>FB</td>\n",
              "      <td>96844400700_10157493758850701</td>\n",
              "      <td>2019-04-23T10:33:37Z</td>\n",
              "      <td>MARCELLO GEMMATO</td>\n",
              "      <td>M</td>\n",
              "      <td>PPE</td>\n",
              "      <td>FDI</td>\n",
              "      <td>FDI</td>\n",
              "      <td>opposizione</td>\n",
              "      <td>destra</td>\n",
              "      <td>s</td>\n",
              "      <td>Se i musulmani pensano di portare la guerra sa...</td>\n",
              "      <td>270</td>\n",
              "      <td>80</td>\n",
              "      <td>57</td>\n",
              "      <td>33</td>\n",
              "      <td>1729</td>\n",
              "      <td>0</td>\n",
              "      <td>problematico</td>\n",
              "      <td>Rifugiati Musulmani</td>\n",
              "      <td>religioni europa</td>\n",
              "      <td>Comparativa</td>\n",
              "      <td>Neg-comp</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>gruppo</td>\n",
              "      <td>non politico</td>\n",
              "      <td>C'è poco da dire questa è gente che la guerra ...</td>\n",
              "      <td>1</td>\n",
              "      <td>FRATELLIDITALIA.PUGLIA</td>\n",
              "      <td>Se i musulmani pensano di portare la guerra sa...</td>\n",
              "      <td>problematico</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Rifugiati Musulmani</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>16.67</td>\n",
              "      <td>16.67</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>15</td>\n",
              "      <td>53320</td>\n",
              "      <td>FB</td>\n",
              "      <td>911961728894076_2169530686470501</td>\n",
              "      <td>2019-04-17T12:50:26Z</td>\n",
              "      <td>IGOR GELARDA</td>\n",
              "      <td>M</td>\n",
              "      <td>EFDD</td>\n",
              "      <td>LEGA</td>\n",
              "      <td>Lega</td>\n",
              "      <td>governo</td>\n",
              "      <td>destra</td>\n",
              "      <td>i</td>\n",
              "      <td>Un mio particolare ringraziamento va ai Magist...</td>\n",
              "      <td>69</td>\n",
              "      <td>33</td>\n",
              "      <td>14</td>\n",
              "      <td>5</td>\n",
              "      <td>6565</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>Other</td>\n",
              "      <td>Comparativa</td>\n",
              "      <td>Neg-comp</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>gruppo</td>\n",
              "      <td>non politico</td>\n",
              "      <td>Escremento umano!</td>\n",
              "      <td>1</td>\n",
              "      <td>gelardaigor</td>\n",
              "      <td>Un mio particolare ringraziamento va ai Magist...</td>\n",
              "      <td>problematico</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Rifugiati</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>4.76</td>\n",
              "      <td>4.76</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.38</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.38</td>\n",
              "      <td>0</td>\n",
              "      <td>4.76</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>16.67</td>\n",
              "      <td>4.76</td>\n",
              "      <td>11.90</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>16</td>\n",
              "      <td>78041</td>\n",
              "      <td>FB</td>\n",
              "      <td>667483386685540_1869411966492670</td>\n",
              "      <td>2019-05-21T15:13:32Z</td>\n",
              "      <td>SILVIA SERAFINA DETTA NARDONE SARDONE</td>\n",
              "      <td>F</td>\n",
              "      <td>EFDD</td>\n",
              "      <td>LEGA</td>\n",
              "      <td>Lega</td>\n",
              "      <td>governo</td>\n",
              "      <td>destra</td>\n",
              "      <td>no</td>\n",
              "      <td>Minacce, insulti, scontri in piazza per blocca...</td>\n",
              "      <td>2121</td>\n",
              "      <td>643</td>\n",
              "      <td>702</td>\n",
              "      <td>1</td>\n",
              "      <td>113152</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>europa altroPolitico</td>\n",
              "      <td>Comparativa</td>\n",
              "      <td>Neg-comp</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>gruppo</td>\n",
              "      <td>non politico</td>\n",
              "      <td>Se l'infilino nei loro culetti antifa a mo di ...</td>\n",
              "      <td>1</td>\n",
              "      <td>silviasardone</td>\n",
              "      <td>Minacce, insulti, scontri in piazza per blocca...</td>\n",
              "      <td>problematico</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Altro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.56</td>\n",
              "      <td>5.13</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>2.56</td>\n",
              "      <td>2.56</td>\n",
              "      <td>0</td>\n",
              "      <td>2.56</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.56</td>\n",
              "      <td>2.56</td>\n",
              "      <td>15.38</td>\n",
              "      <td>10.26</td>\n",
              "      <td>5.13</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>17</td>\n",
              "      <td>229</td>\n",
              "      <td>FB</td>\n",
              "      <td>667483386685540_1844118159022051</td>\n",
              "      <td>2019-05-05T08:53:55Z</td>\n",
              "      <td>SILVIA SERAFINA DETTA NARDONE SARDONE</td>\n",
              "      <td>F</td>\n",
              "      <td>EFDD</td>\n",
              "      <td>LEGA</td>\n",
              "      <td>Lega</td>\n",
              "      <td>governo</td>\n",
              "      <td>destra</td>\n",
              "      <td>no</td>\n",
              "      <td>Ecco il pensiero dei radical chic di sinistra....</td>\n",
              "      <td>1040</td>\n",
              "      <td>1450</td>\n",
              "      <td>2291</td>\n",
              "      <td>9</td>\n",
              "      <td>113152</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>rifugiati europa</td>\n",
              "      <td>Comparativa</td>\n",
              "      <td>Neg-comp</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>gruppo</td>\n",
              "      <td>non politico</td>\n",
              "      <td>pezzo di merda perche non vai via dal italia,s...</td>\n",
              "      <td>1</td>\n",
              "      <td>silviasardone</td>\n",
              "      <td>Ecco il pensiero dei radical chic di sinistra....</td>\n",
              "      <td>problematico</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Altro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>3.23</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>3.23</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>9.68</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>35.48</td>\n",
              "      <td>3.23</td>\n",
              "      <td>3.23</td>\n",
              "      <td>3.23</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>19.35</td>\n",
              "      <td>0.00</td>\n",
              "      <td>6.45</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>20</td>\n",
              "      <td>17457</td>\n",
              "      <td>FB</td>\n",
              "      <td>667483386685540_1835929416507592</td>\n",
              "      <td>2019-04-29T15:12:05Z</td>\n",
              "      <td>SILVIA SERAFINA DETTA NARDONE SARDONE</td>\n",
              "      <td>F</td>\n",
              "      <td>EFDD</td>\n",
              "      <td>LEGA</td>\n",
              "      <td>Lega</td>\n",
              "      <td>governo</td>\n",
              "      <td>destra</td>\n",
              "      <td>no</td>\n",
              "      <td>I vermi protagonisti delle ultime violenze sul...</td>\n",
              "      <td>2335</td>\n",
              "      <td>571</td>\n",
              "      <td>445</td>\n",
              "      <td>13</td>\n",
              "      <td>113152</td>\n",
              "      <td>0</td>\n",
              "      <td>negativo</td>\n",
              "      <td>None</td>\n",
              "      <td>Other</td>\n",
              "      <td>Comparativa</td>\n",
              "      <td>Neg-comp</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Categoria di persone</td>\n",
              "      <td>gruppo</td>\n",
              "      <td>non politico</td>\n",
              "      <td>Anche non chimica ,basta castrare</td>\n",
              "      <td>1</td>\n",
              "      <td>silviasardone</td>\n",
              "      <td>I vermi protagonisti delle ultime violenze sul...</td>\n",
              "      <td>problematico</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Altro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.70</td>\n",
              "      <td>0.47</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.23</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.23</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.86</td>\n",
              "      <td>0.23</td>\n",
              "      <td>2.33</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.93</td>\n",
              "      <td>0.70</td>\n",
              "      <td>0</td>\n",
              "      <td>2.80</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.40</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.23</td>\n",
              "      <td>30.07</td>\n",
              "      <td>3.50</td>\n",
              "      <td>10.72</td>\n",
              "      <td>1.17</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.47</td>\n",
              "      <td>0.23</td>\n",
              "      <td>0.93</td>\n",
              "      <td>0.93</td>\n",
              "      <td>11.19</td>\n",
              "      <td>0.93</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10098</th>\n",
              "      <td>77924</td>\n",
              "      <td>41072</td>\n",
              "      <td>Twitter</td>\n",
              "      <td>1.11772429491684E+018</td>\n",
              "      <td>2019-04-15T09:40:12Z</td>\n",
              "      <td>ANTONIO TAJANI</td>\n",
              "      <td>M</td>\n",
              "      <td>PPE</td>\n",
              "      <td>FI</td>\n",
              "      <td>FI</td>\n",
              "      <td>opposizione</td>\n",
              "      <td>destra</td>\n",
              "      <td>c</td>\n",
              "      <td>In viaggio per Strasburgo. In agenda per quest...</td>\n",
              "      <td>23</td>\n",
              "      <td>17</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>6222</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>europa clima</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td></td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>@Antonio_Tajani @Utente_Generico @Utente_Gener...</td>\n",
              "      <td>1</td>\n",
              "      <td>Antonio_Tajani</td>\n",
              "      <td>In viaggio per Strasburgo. In agenda per quest...</td>\n",
              "      <td>negativo</td>\n",
              "      <td>negativo</td>\n",
              "      <td>civile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>62.50</td>\n",
              "      <td>12.50</td>\n",
              "      <td>0.00</td>\n",
              "      <td>6.25</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>12.50</td>\n",
              "      <td>31.25</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10099</th>\n",
              "      <td>77928</td>\n",
              "      <td>43438</td>\n",
              "      <td>Twitter</td>\n",
              "      <td>1.11771528814812E+018</td>\n",
              "      <td>2019-04-15T09:04:25Z</td>\n",
              "      <td>DAVID SASSOLI</td>\n",
              "      <td>M</td>\n",
              "      <td>PSE</td>\n",
              "      <td>Siamo Europei</td>\n",
              "      <td>PD</td>\n",
              "      <td>opposizione</td>\n",
              "      <td>sinistra</td>\n",
              "      <td>c</td>\n",
              "      <td>Dalla Conferenza Programmatica della Federazio...</td>\n",
              "      <td>20</td>\n",
              "      <td>9</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>19167</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>europa</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td></td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>@DavidSassoli @Utente_Generico @Utente_Generic...</td>\n",
              "      <td>1</td>\n",
              "      <td>DavidSassoli</td>\n",
              "      <td>Dalla Conferenza Programmatica della Federazio...</td>\n",
              "      <td>negativo</td>\n",
              "      <td>negativo</td>\n",
              "      <td>civile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.08</td>\n",
              "      <td>0</td>\n",
              "      <td>2.08</td>\n",
              "      <td>2.08</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>22.92</td>\n",
              "      <td>8.33</td>\n",
              "      <td>4.17</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>2.08</td>\n",
              "      <td>2.08</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>6.25</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10100</th>\n",
              "      <td>77963</td>\n",
              "      <td>79121</td>\n",
              "      <td>FB</td>\n",
              "      <td>56413702888_10157226250102889</td>\n",
              "      <td>2019-05-18T15:50:12Z</td>\n",
              "      <td>DANIELA SANTANCHÉ</td>\n",
              "      <td>F</td>\n",
              "      <td>PPE</td>\n",
              "      <td>FDI</td>\n",
              "      <td>FDI</td>\n",
              "      <td>opposizione</td>\n",
              "      <td>destra</td>\n",
              "      <td>no</td>\n",
              "      <td>Un’altra eccellenza italiana, la famiglia Ravi...</td>\n",
              "      <td>57</td>\n",
              "      <td>4</td>\n",
              "      <td>8</td>\n",
              "      <td>1</td>\n",
              "      <td>15001</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>Other</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td></td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Imbec... fatti scuoiare</td>\n",
              "      <td>1</td>\n",
              "      <td>danielasantanche</td>\n",
              "      <td>Un’altra eccellenza italiana, la famiglia Ravi...</td>\n",
              "      <td>hate</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Altro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>4.08</td>\n",
              "      <td>4.08</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4.08</td>\n",
              "      <td>2.04</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>42.86</td>\n",
              "      <td>4.08</td>\n",
              "      <td>6.12</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>12.24</td>\n",
              "      <td>12.24</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4.08</td>\n",
              "      <td>0.00</td>\n",
              "      <td>4.08</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10101</th>\n",
              "      <td>77993</td>\n",
              "      <td>80527</td>\n",
              "      <td>FB</td>\n",
              "      <td>252306033154_10156588128813155</td>\n",
              "      <td>2019-05-04T14:46:05Z</td>\n",
              "      <td>MATTEO SALVINI</td>\n",
              "      <td>M</td>\n",
              "      <td>EFDD</td>\n",
              "      <td>LEGA</td>\n",
              "      <td>Lega</td>\n",
              "      <td>governo</td>\n",
              "      <td>destra</td>\n",
              "      <td>tutte</td>\n",
              "      <td>🔴Quasi il 60% degli italiani è favorevole alla...</td>\n",
              "      <td>96798</td>\n",
              "      <td>8516</td>\n",
              "      <td>7108</td>\n",
              "      <td>2</td>\n",
              "      <td>2186542</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>Other</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td></td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Mario ...penso che chi si stia rincoglionendo ...</td>\n",
              "      <td>2</td>\n",
              "      <td>Anonymous</td>\n",
              "      <td>È in atto un rincoglionimento totale, far scon...</td>\n",
              "      <td>hate</td>\n",
              "      <td>probl-hate</td>\n",
              "      <td>incivile</td>\n",
              "      <td>negativo</td>\n",
              "      <td>Altro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.75</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.75</td>\n",
              "      <td>0</td>\n",
              "      <td>3.51</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>33.33</td>\n",
              "      <td>5.26</td>\n",
              "      <td>3.51</td>\n",
              "      <td>1.75</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.75</td>\n",
              "      <td>1.75</td>\n",
              "      <td>0.00</td>\n",
              "      <td>3.51</td>\n",
              "      <td>1.75</td>\n",
              "      <td>3.51</td>\n",
              "      <td>10.53</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10102</th>\n",
              "      <td>78060</td>\n",
              "      <td>79405</td>\n",
              "      <td>FB</td>\n",
              "      <td>56413702888_10157186418942889</td>\n",
              "      <td>2019-05-03T05:28:20Z</td>\n",
              "      <td>DANIELA SANTANCHÉ</td>\n",
              "      <td>F</td>\n",
              "      <td>PPE</td>\n",
              "      <td>FDI</td>\n",
              "      <td>FDI</td>\n",
              "      <td>opposizione</td>\n",
              "      <td>destra</td>\n",
              "      <td>no</td>\n",
              "      <td>Il mio intervento ieri sera nella trasmissione...</td>\n",
              "      <td>56</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>1</td>\n",
              "      <td>15001</td>\n",
              "      <td>0</td>\n",
              "      <td>positivo</td>\n",
              "      <td>None</td>\n",
              "      <td>Other</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>Positiva</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td></td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>1) violenza sessuale: minimo 30 anni, con obbl...</td>\n",
              "      <td>1</td>\n",
              "      <td>danielasantanche</td>\n",
              "      <td>Il mio intervento ieri sera nella trasmissione...</td>\n",
              "      <td>ambiguo</td>\n",
              "      <td>positivo</td>\n",
              "      <td>civile</td>\n",
              "      <td>positivo</td>\n",
              "      <td>Altro</td>\n",
              "      <td>NaN</td>\n",
              "      <td>...</td>\n",
              "      <td>1.85</td>\n",
              "      <td>1.85</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>3.70</td>\n",
              "      <td>3.70</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1.85</td>\n",
              "      <td>3.70</td>\n",
              "      <td>0</td>\n",
              "      <td>1.85</td>\n",
              "      <td>1.85</td>\n",
              "      <td>1.85</td>\n",
              "      <td>1.85</td>\n",
              "      <td>0.00</td>\n",
              "      <td>7.41</td>\n",
              "      <td>11.11</td>\n",
              "      <td>1.85</td>\n",
              "      <td>5.56</td>\n",
              "      <td>1.85</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.85</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>10103 rows × 246 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "       Unnamed: 0  Origin_file_order     Site  ... p_OtherP Count target1_2\n",
              "0               0              30126       FB  ...     0.00     1       NaN\n",
              "1              15              53320       FB  ...     0.00     1       NaN\n",
              "2              16              78041       FB  ...     0.00     1       NaN\n",
              "3              17                229       FB  ...     0.00     1       NaN\n",
              "4              20              17457       FB  ...     0.93     1       NaN\n",
              "...           ...                ...      ...  ...      ...   ...       ...\n",
              "10098       77924              41072  Twitter  ...    31.25     1       NaN\n",
              "10099       77928              43438  Twitter  ...     0.00     1       NaN\n",
              "10100       77963              79121       FB  ...     4.08     1       NaN\n",
              "10101       77993              80527       FB  ...    10.53     1       NaN\n",
              "10102       78060              79405       FB  ...     0.00     1       NaN\n",
              "\n",
              "[10103 rows x 246 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4ZiBonDIMapF"
      },
      "source": [
        "Trial and Error (To be ignored):"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "wzxKqqNIxdTF",
        "outputId": "b482c5f2-56d0-4994-f082-b0ff5b3efb11"
      },
      "source": [
        "hate_comments = df_post[\"c_Emo_Neg\"] \r\n",
        "#hate_comments\r\n",
        "\r\n",
        "hate_posts = df_post[\"p_Emo_Neg\"]\r\n",
        "#hate_posts\r\n",
        "\r\n",
        "\r\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        0.00\n",
              "1        0.00\n",
              "2        0.00\n",
              "3        6.45\n",
              "4        0.70\n",
              "         ... \n",
              "10098    0.00\n",
              "10099    2.08\n",
              "10100    4.08\n",
              "10101    1.75\n",
              "10102    3.70\n",
              "Name: p_Emo_Neg, Length: 10103, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "wZkZ2CIAzngj",
        "outputId": "e73a4cd4-021b-40b7-aeec-763808cf7f45"
      },
      "source": [
        "corr = np.corrcoef(hate_posts, hate_comments)\r\n",
        "plt.plot(corr)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f4a4d709358>,\n",
              " <matplotlib.lines.Line2D at 0x7f4a4d709080>]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "FDlB2SE00tJW",
        "outputId": "1fab01d4-cfc5-4e2e-d689-85513dc7086f"
      },
      "source": [
        "print(corr)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1.         0.05976614]\n",
            " [0.05976614 1.        ]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 285
        },
        "id": "dMESduUc0vhm",
        "outputId": "5d676f8f-b0c6-4b92-cceb-ee3ddcc07e68"
      },
      "source": [
        "corr_pearson = hate_posts.corr(hate_comments)\r\n",
        "plt.plot(corr_pearson)\r\n",
        "print(corr_pearson)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.05976614480766517\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "jKzijiLz8WLj",
        "outputId": "453fd746-c01c-4cdc-e4a1-2ef726809e5b"
      },
      "source": [
        " lin_reg = stats.linregress(hate_posts, hate_comments) \r\n",
        " plt.plot(lin_reg)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f4a4d1bd6d8>]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UMxhgRGRAcOl"
      },
      "source": [
        "# Useful Part:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mdZYlUVwMSfG"
      },
      "source": [
        "## Negative Emotions"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "mIpuzGP_-F5W",
        "outputId": "2d0fc55f-7321-45ab-f0a6-998357542372"
      },
      "source": [
        "correlation_coeff = np.corrcoef(hate_posts, hate_comments)\r\n",
        "display(correlation_coeff)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(hate_posts, hate_comments)\r\n",
        "plt.show()"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.05976614],\n",
              "       [0.05976614, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3dfXAc9Z3n8XfPjJ8kWQ8jyVZs4wVhE8dewRZnn52sWRFQnDoga3aPdYozYV2cN3U4OF7F3AU2rOM1EFQbFAlYU2wWyg7gu5CrHPbeHrukFApvkRSJWPPgtWPHGIcQjKyHkWQ9+UEzfX+0JUua7pme0WhmuvV5VaWCevrhq7b9VevX39/3Z5imaSIiIr4SyHUAIiKSeUruIiI+pOQuIuJDSu4iIj6k5C4i4kNK7iIiPhTKdQAjTp8+ndZxFRUVdHZ2Zjiaqae4s8eLMYPiziYvxgywYMECx8/05C4i4kNK7iIiPqTkLiLiQ0ruIiI+pOQuIuJDSatlnn76aQ4dOkRJSQmNjY0A9Pf309TUREdHB5WVldTX11NUVIRpmuzZs4e3336bWbNmsWXLFqqrq6ck8Ohj/wM+OMaZkQ3Vywg++LcAxDra4MA+zN9+AGc+hljM2icYgtIwbNqGUV5p7dMTgdlzoO8s/Pakte/sOXBuCEwTDOPy14EALPkMxt33Wee7dLxRGob1GwlUVjnGOxrTpet1z5xF9GxPwmPHHmOUhjHXrsN44yeOX4+cZ+JxyWITEf8xknWFPHr0KLNnz2b37t2jyf3FF1+kqKiI22+/nf3799Pf389dd93FoUOH+Jd/+RcefPBBTpw4wd69e/nOd77jKpBUSiFHEnuc6mUYm7+B2bQDOtoSnMGAkjLojbi+5jiFc2HWbIh0XN5WWYVRv8sxSSeMyeZY22MCQYhFnb+urIK7t8LzT40/LkFsqfJiyZgXYwbFnU1ejBkmWQq5fPlyioqKxm1rbW2ltrYWgNraWlpbWwF46623+KM/+iMMw+Caa65hYGCA7u7uycRuzy6xj2w/sC9JYgcw00/sAAN94xM7WNc8sM9+/2Qx2R1rd8zYRG73dUcb7H0i/rhEsYmIL6U1iam3t5eysjIASktL6e3tBSASiVBRUTG6X3l5OZFIZHTfsVpaWmhpaQGgoaFh3HHJnEnwWWigj4uuz5RZoYE+wjbfR8RFTBOPdXOMraHBlGJLVSgUSunPKh94MWZQ3NnkxZiTmfQMVcMwMAwj5ePq6uqoq6sb/TpTvxINF87NyHnSvbbd9xFzEdPEY90cY2tOAQz2u44tVV789dWLMYPiziYvxgxTMEO1pKRkdLilu7ub4uJiAMLh8Lgb1NXVRTgcTucSiVUvc96+fqM19pyQASWTiKtwLoQrx2+rrLKubSdZTHbH2h0TCCb+urIKNm2LPy5RbCLiS8GdO3fuTLbTwMAAP/vZz/jiF78IWE/Zn3zyCcuWLePVV1+lsrKSa6+9FsMw+OlPf8ratWs5ceIER44c4bbbbnMVSF9fn+ugAzd8AfPI29A95iftpWoZo7AIrl2F0X/WqnwZ7LeqXsCqlglXwJa/wvjCemufomJYdKWVsPt6AQPmFEI0av13IHD562AIrvl9jK1/jfG5m0ePN5Z8BmPTNscXluNiunS9mYuric4tcTx24jHGks/AlzdjxKKOXxubthH8vavjjksUW6oKCgoYHLQf+slXXowZFHc2eTFmgLlznX/DT1ot09zczNGjR+nr66OkpIQNGzawatUqmpqa6OzsjCuFfO6553j33XeZOXMmW7Zs4eqrr3YVpBqHeYMX4/ZizKC4s8mLMUPiYZmkyT1blNy9wYtxezFmUNzZ5MWYQV0hRUSmHSV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxodBkDv6nf/onXnvtNQzD4IorrmDLli309PTQ3NxMX18f1dXVbN26lVBoUpcREZEUpf3kHolE+Od//mcaGhpobGwkFovx85//nBdffJFbb72Vp556isLCQl577bVMxisiIi5MalgmFotx4cIFotEoFy5coLS0lCNHjrBmzRoAbrzxRlpbWzMSqIiIuJf2eEk4HOZLX/oS9957LzNnzuS6666jurqagoICgsHg6D6RSMT2+JaWFlpaWgBoaGigoqIirThCoVDax+aS4s4eL8YMijubvBhzMmkn9/7+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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 301
        },
        "id": "Pxp3PB6BAj_g",
        "outputId": "47d13dd4-725f-4c87-df5a-f65d96e9ba78"
      },
      "source": [
        "hate_corr = postDB.loc[postDB['c_rating']=='hate']\r\n",
        "hate_corr\r\n",
        "\r\n",
        "correlation_coeff_2 = np.corrcoef(hate_corr[\"p_Emo_Neg\"], hate_corr[\"c_Emo_Neg\"])\r\n",
        "display(correlation_coeff_2)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(hate_corr[\"p_Emo_Neg\"], hate_corr[\"c_Emo_Neg\"])\r\n",
        "plt.show()"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[ 1.        , -0.23772203],\n",
              "       [-0.23772203,  1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "nqHgXE4eC22w",
        "outputId": "cbef3396-20fb-4bad-960f-d2383c41afb8"
      },
      "source": [
        "problematic_corr = postDB.loc[postDB['c_rating']=='problematico']\r\n",
        "problematic_corr\r\n",
        "\r\n",
        "correlation_coeff_3 = np.corrcoef(problematic_corr[\"p_Emo_Neg\"], problematic_corr[\"c_Emo_Neg\"])\r\n",
        "display(correlation_coeff_3)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(problematic_corr[\"p_Emo_Neg\"], problematic_corr[\"c_Emo_Neg\"])\r\n",
        "plt.show()"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.04144285],\n",
              "       [0.04144285, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3de3RU5d0v8O+eGblMLpNMZiAG9JUgSuUFrQ2F4y2IkbOOtoW6POlSlJeXw+FoFCG1vkLry7K0vmRVY5AC1R4sKLpeUZeA7bFeUk7CsVYNV0OUoJBW2xBymRAmFy6Z2eePnRlmMnvP7D2z91x2vp+1XJJn3357MvPLM89+LoIoiiKIiMhULKkOgIiI9MfkTkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEK2VAcQ0NraGtdxLpcLnZ2dOkeTOMalDePSLl1jY1zaJBJXUVGR4jbW3ImITIjJnYjIhJjciYhMiMmdiMiEmNyJiEwoZm+ZzZs348CBA3A4HKiurgYA9Pb2oqamBh0dHXC73aisrER2djZEUcTWrVtx8OBBjB49GhUVFSguLjYkcN/RRmDbczg10A+MtQOLV8A6dboh19LC39EG7H4Vnj4v/Fk5wPyFsLgLw7aJpz0Q8pxh28xiJNwjUSaIWXOfM2cOfvrTn4aV7dq1C9OnT8eGDRswffp07Nq1CwBw8OBBtLW1YcOGDVi2bBm2bNliSNC+o41AzRqgqx3o75X+X7NGKk8hf0cbxJo1ED+px4UjByB+Ug+xZg38HW1h29DcGLbNLEbCPRJlipjJ/ZprrkF2dnZYWUNDA0pLSwEApaWlaGhoAADs27cPt9xyCwRBwFVXXYW+vj50d3frH/W25wC/L7zM75PKU2n3q8DwRDZUk426zSxGwj0SZYi4BjH19PQgPz8fAJCXl4eenh4AgMfjgcvlCu5XUFAAj8cT3DdUbW0tamtrAQBVVVVhx8VyaqBffsNAv6bz6M3T58UFmXJbnxcAFLc5kxizzWYz7DWKdv+x7tHIuBKRrnEB6Rsb49LGqLgSHqEqCAIEQdB8XFlZGcrKyoI/axqhNdYuNcfIlKdyBJo/K0e2fFChPLAtmTEbOUov2v3HuqYZRw8aLV1jY1zapNUIVYfDEWxu6e7uRm5uLgDA6XSGBdnV1QWn0xnPJaJbvAKwWMPLLFapPJXmLwSGPzx0F0rl0baZxUi4R6IMEVdyLykpQX19PQCgvr4eM2fODJbv3bsXoiji2LFjsNvtsk0yibJOnQ5UrgUKxgH2bOn/lWtT3lvG4i6EULkWwqxSXPLP10OYVQqhci0s7sKwbbh6etg2sxgJ90iUKYRYa6iuX78en3/+ObxeLxwOB8rLyzFz5kzU1NSgs7Mzoivkiy++iMOHD2PUqFGoqKjA5MmTVQXCicOSg3Fpk65xAekbG+PSxqhmmZht7itXrpQtX7NmTUSZIAhYunSphtCIiMgIHKFKRGRCTO5ERCbE5E5EZEJM7kREJsTkTkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEJM7kREJsTkTkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEJM7kREJsTkTkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEJM7kREJsTkTkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEJM7kREJsTkTkRkQkzuREQmxORORGRCtkQO/sMf/oA9e/ZAEARcdtllqKiowOnTp7F+/Xp4vV4UFxdj+fLlsNkSugwREWkUd83d4/Hgj3/8I6qqqlBdXQ2/34+PPvoIr7zyCu688078+te/RlZWFvbs2aNnvEREpEJCzTJ+vx/nz5+Hz+fD+fPnkZeXh6amJsyePRsAMGfOHDQ0NOgSKBERqRd3e4nT6cT3v/99PPjggxg1ahSuvfZaFBcXw263w2q1BvfxeDyyx9fW1qK2thYAUFVVBZfLFVccNpst7mONxLi0YVzapWtsjEsbo+KKO7n39vaioaEBmzZtgt1ux7PPPotDhw6pPr6srAxlZWXBnzs7O+OKw+VyxX2skRiXNoxLu3SNjXFpk0hcRUVFitviTu6NjY0YN24ccnNzAQCzZs1Cc3Mz+vv74fP5YLVa4fF44HQ6470EERHFKe42d5fLhS+//BLnzp2DKIpobGzExIkTMW3aNHz88ccAgLq6OpSUlOgWLBERqRN3zX3KlCmYPXs2Hn/8cVitVlxxxRUoKyvD9ddfj/Xr1+O1117DpEmTMHfuXD3jJSIiFRLqgF5eXo7y8vKwsvHjx2PdunUJBUVERInhCFUiIhNiciciMiEmdyIiE2JyJyIyISZ3IiITYnInIjIhJnciIhNiciciMiEmdyIiE2JyJyIyISZ3IiITYnInIjIhJnciIhNiciciMiEmdyIiE2JyJyIyISZ3IiITYnInIjIhJnciIhNiciciMiEmdyIiE2JyJyIyISZ3IiITYnInIjIhJnciIhNiciciMiEmdyIiE2JyJyIyISZ3IiITYnInIjIhWyIH9/X14fnnn8c333wDQRDw4IMPoqioCDU1Nejo6IDb7UZlZSWys7P1ipeIiFRIKLlv3boV1113HR599FEMDg7i3Llz2LlzJ6ZPn44FCxZg165d2LVrF+677z694iUiIhXibpbp7+/HF198gblz5wIAbDYbsrKy0NDQgNLSUgBAaWkpGhoa9ImUiIhUi7vm3t7ejtzcXGzevBl/+9vfUFxcjMWLF6Onpwf5+fkAgLy8PPT09MgeX1tbi9raWgBAVVUVXC5XXHHYbLa4jzUS49KGcWmXrrExLm2Miivu5O7z+dDS0oIlS5ZgypQp2Lp1K3bt2hW2jyAIEARB9viysjKUlZUFf+7s7IwrDpfLFfexRmJc2jAu7dI1NsalTSJxFRUVKW6Lu1mmoKAABQUFmDJlCgBg9uzZaGlpgcPhQHd3NwCgu7sbubm58V6CiIjiFHdyz8vLQ0FBAVpbWwEAjY2NmDhxIkpKSlBfXw8AqK+vx8yZM/WJlIiIVEuot8ySJUuwYcMGDA4OYty4caioqIAoiqipqcGePXuCXSGJiCi5EkruV1xxBaqqqiLK16xZk8hpiYgoQRyhSkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEJM7kREJsTkTkRkQkzuREQmxORORGRCTO5ERCbE5E5EZEIJzS2TSr5Xnwfq3sGpQMGcO2Bd+EAqQwIA+DvagN2vwtPnhT8rB5i/EBZ3YarDIqIRJiOTeyCxh6l7Bz4gpQne39EGsWYN0NGGC4HCE83wV65lgieipMrMZpnhiT1WebLsfhXoaAsvG6rJExElU2Ym9zQlnvZoKiciMgqTu46EPKemciIio2Rmcp9zh7byZJm/EBjetu4ulMqJiJIoIx+oWhc+AB8Q3saeBr1lLO5C+CvXArtfha3Pi0H2liGiFMnI5A4M9YpZ+ABcLhc6OztTHU6QxV0ILH0UzjSLi4hGlsxsliEioqiY3ImITIjJnYjIhJjciYhMiMmdiMiEmNyJiEyIyZ2IyISY3ImITIjJnYjIhJjciYhMiMmdiMiEmNyJiEwo4YnD/H4/Vq1aBafTiVWrVqG9vR3r16+H1+tFcXExli9fDpstY+cnUxRYK1U87ZHma49j9kc9zkFEJCfhrPvOO+9gwoQJGBgYAAC88soruPPOO3HjjTfit7/9Lfbs2YN58+YlHGg6CV0rFQBEQPNaqXqcg4hISULNMl1dXThw4ABuu+02AIAoimhqasLs2bMBAHPmzEFDQ0PiUaYbPdZK5XqrRGSghGru27Ztw3333RestXu9XtjtdlitVgCA0+mExyO/fmhtbS1qa2sBAFVVVXC5XHHFYLPZ4j42Xp4+Ly7IxdLnhXMollhxqTmHEVLxeqnBuLRL19gYlzZGxRV3ct+/fz8cDgeKi4vR1NSk+fiysjKUlZUFf453YYtULNbhz8qRLR/MygnGEisuNecwQrotbhLAuLRL19gYlzaJxFVUVKS4Le7k3tzcjH379uHgwYM4f/48BgYGsG3bNvT398Pn88FqtcLj8cDpNOHi0PMXAieaw5tVtK6Vqsc5iIgUxJ3c7733Xtx7770AgKamJvz+97/HI488gmeffRYff/wxbrzxRtTV1aGkpES3YNNF6Fqp8fZ00eMcRERKdO+juHDhQqxfvx6vvfYaJk2ahLlz5+p9ibQQWCs11ecgIpKjS3KfNm0apk2bBgAYP3481q1bp8dpiYgoThyhSkRkQkzuREQmxORORGRCTO5ERCaUsTN6+T54G3jzdzjl9wMWC3D3Elhv/4Fu5482qZfcNgBhZWfvLIf//7yeUd0cOZEZkXlkZHL3ffA28PqWiwV+P/D6FvgAXRJ8tEm9AERuO9YECALg6QiW9ez7EPD5Io5P12TJicyIzCUzm2Xe/J22cq2iTeolt627M5jYg4YSe8Tx6YoTmRGZSkbW3OH3ayvXSDwtP9mZUnmi500HRt0zEaVGZiZ3i0U+kVv0+SIi5DmlZgmZcgCy29SeN13FumciyiyZ2Sxz9xJt5VrNXyhN4hUqMKmX3LZ8F+B0h5cNTXsccXy6inbPRJRxMrLmbr39B/ABUhu7Ab1lYk3qJbcNQFhZ7p3lOJNBvWU4kRmRuQiiKMbbyqCr1tbWuI4z4xzNRmJc2qRrXED6xsa4tDFqPvfMbJYhIqKoMrJZBrg44MbT55VWNUqjJgR/Rxt6tm+E79RJNm8QUUpkZHIPHXATXIc0TQbcBGI7y8FARJRCmdksk84DbtI5NiIaMTIyuafzgJt0jo2IRo6MTO5KA2vSYcBNOsdGRCNHRib3tB5wk86xEdGIkZEPVEMH3Nj6vBhMo94ygdhGv/smzrK3DBGlSEYmdwAQ398FfFJ/sbfM2Cxg4QOqjjV63nKLuxCOyidxQWZggpprZ/K86r6jjcC254D+PsCeBSxeAevU6akOi2jEycjk7nv1eaDunfDCunek+dxjJPhUzluu5tqZPK+672gjULMG8A9NdzzQB9Ssga9yLRM8UZJlZpv78MQeqzxUKrsqqrl2Jnel3PbcxcQe4PdJ5USUVJmZ3BOQyq6Kaq6d0V0p+/u0lRORYUZcck9lV0U1187orpT2LG3lRGSYzEzus+ZoKw+Vyq6Kaq6dyV0pF68ALMPmsbdYpXIiSqqMfKAqQJRfNUjFGkmpnLdczbUzeV5169Tp8FWuZW8ZojSQkcldbG+TLx/+IFKBxV0ILH1Uz5BUU3PtVMaXKOvU6UDVllSHQTTiZWazzJlu+fIehXIiohEmM5N7bp62ciKiESbuZpnOzk5s2rQJp0+fhiAIKCsrwx133IHe3l7U1NSgo6MDbrcblZWVyM7O1jNmCOMuhdhyTLZcL3qPEk3lqFN/RxvEHVuAE81ot1ggXjEFwo+Whg2cwu5XIbafBM6cBnLzIYwrzJi2fiKKFHdyt1qtuP/++1FcXIyBgQGsWrUKM2bMQF1dHaZPn44FCxZg165d2LVrF+677z49Y4b4j280lWul9yjRlI+KfeZngKfj4rUPfwrx6xPwP/YfUllIbACArnaILc0ZMzKWiCLF3SyTn5+P4uJiAMDYsWMxYcIEeDweNDQ0oLS0FABQWlqKhoYGfSIN9fcT2sq10nuUaKpHxQ4l9jDdndI2udgCMmVkLBFF0KW3THt7O1paWnDllVeip6cH+fn5AIC8vDz09PTIHlNbW4va2loAQFVVFVwul+rrnYqyTct5lHj6vBcnJAth6/PCqfL8NpstGIse54uX0rUD1weguD2wj9ExAuGvVzpJ17iA9I2NcWljVFwJJ/ezZ8+iuroaixcvht1uD9smCAIEQZA9rqysDGVlZcGfO2VmUIyHHufxZ+XIlg9m5ag+v8vlCu6rx/nipXTtwPVjSUaMQPjrlU7SNS4gfWNjXNokEldRUZHitoR6ywwODqK6uho333wzZs2aBQBwOBzo7pa6JHZ3dyM3NzeRS8grnqqtXCu9R4mmelSs0x1Znu+StsnFFpApI2OJKIL1ySeffDKeA0VRxG9+8xu4XC6Ul5cHyzs7O3Hy5ElMnToV7733HtxuN2bMmBHzfF6vV/W1LTffDrHpoNRuHFA8FdbVv9J0D0qErGxgxkwIvWeA7FwIV34LwuIVmh4s2u129Pf363a+eAlZ2cB1s4DOU0B/L4SxdmDqDAjLHoPFXRge26jRgNUKXDoRwlX/nLQYgfDXK52ka1xA+sbGuLRJJK6cHOVv33E3yzQ3N2Pv3r24/PLL8dhjjwEA7rnnHixYsAA1NTXYs2dPsCtkJop3lGigW6Gnzys1iQx1J5Q7X7K6R1rchfD/aOnFlavGjI3YHu+IWD3vgQt9EOlHEEUx9oQsSdDa2qp6X9+6fwNOHI3coGPtPR7DuzwCANyFEGS6E2rZN5lxpeq82Se/Qc+Tj4TPB2+xAile6CNd22mB9I2NcWmTlm3uKSOX2KOVJ4uWLo/J7B5p1LV0PK934y+40AeRjjJy4rB0pWWhjWQuyqH2WlqbWPS8B39vr/wGLvRBFBcmdx0JeU75qYhlFtrQsm8y4opnFG2s82r5Y2HJzoa/XybBc6EPoriMmOSelIeX8xcCJ5oj2qDFm+bBv6U67NpK+2L+Qv0fLM5fCHz5efhIVasN4tFG+P7jJ9JcPWcHlJtYlB62RrkHrX8sch7+d/k2dy70QRSXEZHckzW3S+hCG7Y+LwazciDeNA94+dfBueYD1xYq10KQWZRD7OoAatZcTHIDfUDNGvgSfbA4/Lm5bxDo8QA9HmkSNpv8WyHaHPnRFhbxb6nW9MdizPRvo4cLfRDpZkQkd6UHf+LLm+DrOBmRTPSq5YtnB4At1VISHX7t6icgPPpLWIYlOl/1E8oPFuNdBGP3q+FjAuQMDsqXx5gjX6kbZTzt8VzoI/2kcjZTSsyISO6KCeXo4Yv/DtSQl6wM+2MQrZY//I0fqKWjoy3qfC0ApJkXa9ZINV8geB50d8nvr/BgUc2HL6GHtBrnyA/Eg9av5XfoPAXfMz9josgAqZzNlBI3IpK70oO/CH4f8PJG4Py58HKZ5gTZN/6hT4BzZ9UHFphnvfVr5ZkZA0aNjgxX5YdP9f3LiDZHfrQ/brIsVqCrXfrDphArpZFoXV0zdBnIkWREJHfZB38QALmUd0G+zh2o/QYT2pEDQN+wKRO0JPaAE82AV37mzDCXXhZZpvbDJ3v/wzjdUrt8aPNNlLllZP+wNPw/wO+P3DnHIf1x6mqPHWsC2ISgr2R21yX9jYjkLvfgTzzaGNkWDgCXXBJZc4dU+5UdkZksYmTSjPXhC012KLoc6OqIbM8HAEEA/nWl9O/QB5qLlisnR7k/LHKJHZCuDUQm9yj3oBWbEPSXzO66pL8RkdyByAd/vqON4b1SAKnZYNHDkYkrUIONtrBFwOgx6mvw7kIp8R3+NOauWvvKy/4hGjUaOC+T3EUR2Lo+vOY+0Ae8/GvF5KgpKY8ZC2HMWFV97eOuebMJQX9RurpS+hsxyX0469Tp8A3vevfD+yE07oOY7ZBqobl5UpvzUJLxqUlo8+8D/vQ2MNAvJVOnC/j6eHhvFJsNmHY9hB8tBQCIw9vcLdbwPzpON8SzA5EPIqN9+OSS3flzUi1dbjohudWahp4J+MeMjUi4mtvxYySKwbbWhGrebELQX7SurpT+RmxyB8K73gVqumH9us90Q8zNQ2C5EVUJbfcrF2vu/b2AxQLYs6WFpwNy8sIXqB7eZHTTPAgfvi8lpjFjga9PBGv3w5Oeb9Fy2aYUX7vCNwyt88R9fhDi0HOI0GurascPODsQM1H0/edvE6p5swnBGInMGEqplZkThxlBrqZ74YK0mHTNGqnJINrCFgHDm2Q8HeGJHbi4fukQi7sQlqWPQviX5VLBH14DAAj/shzCmLGRfdSHkp6/o03qndLVLjWjdLVLTSkdbcCZ6P3TVRv+gHno2pah2R+FWaVA8dVSc5SCQIIN3Kf1J0/BsvTRsBqgzyPfD191zTuFC6L4O9rg31IN3zM/g39LtfT6E6XYiK65hxLbTypvDBl0JFSuhfjzFcC5gcSuJzNpl1yzBLLlV7IS208C1U8o90DJzZN9gKnI6QYGL4T/IRrePDQs9tBanT/QrfPIfsAXckxgxacYrE6X7NgAuZq3Utt8KpoQ+CCX0hWTO4aShdKgm4ChQUdC5VrZniuaCULYfDOKc7so9UBp/Vrxwa142iPNF9NyLHoMtkuAS0YFnzfgrZeHbbfJPoCVS7iBBUHEb1rC2+8V1tAdLuueZTj7xWcxH97FTKbJbkLgg1xKU0zugPRBVNPDJfCh1WN9kxPNEIe6XIqA1AVTjiNfarcPTSAxeuQEJyeL1SY+eEH6b6AP2L4p8pznz0VeK1pTx+5XIx/MejpUJTpbYZHsXDsRtd8oydQ/9CA5mTV3PsildMXkjhhNMsP3bf0auHA+8YsO70uvMHgKPd3A4hXSA9b2k1KzSW+U9WaHkm9YM8Vn+6QEHo3SH4sJ/wTBXagqYYoK336UyodTU/NWTKbtJ6WurUluHuGDXEpXIyK5yw2TD/ZGESxArOaLUKfULweome0SqSYdqqsd2FIN8dKJwN9blP8IAFIN/9bvQax+Ar6QydAEAOIn9XGFJAw9BFUSNlDqH3+T30nH10yxx9KZ04aPgJXFvuCUpkyf3GXbaD+pj2+ulUtG6dMko+TKa4CvPo9M8ENT88bk9wOvh8yqONAH1Pw7xCWV6rsthrJYpflilC6ndsSuynZ3VYOYlJJptsPQEbBK2Bec0pXpk7uqUaVq6dEco8RiAb5piUzsifL7gTe3Qfi3dRDXPaZuHpvgsT4IH74PKM2prva1VejxE0rtICalZIrdr0JsaY44bzKaR8zcF5zz9WQu0yf3tHywJfdA1O8H+s4Yc73TXVIinnBF+DTHKkR7/bS8tv4t1VETg5ZBTHLJ1D9/ITB8viCHk80jCWA3z8xm6uTu72gDOk+lOoxwFovUth7PDJIR55Lvhy5H/KReuq5G0fqZ4+9/VXeSrnaIXe1RE8OFk/+QPVTtw26xqyNyYZGebqmciSg+7OZpqMDnyNPnhT8rR/dvRaYdoeo72gjx549oG8gTMHqs/gEF+P2RUwXHI8cBTJoi/T/HAVz7XWmag2i0Nvko9TN/5mfSHwut9xFIDDLEHoVFSoaP7lWy7TlETuEsDpVTPNjN0zjB6U4+qceFIwcgflJ/cSS8TkyZ3P0dbcDGX8RfO05w9GlSeHuA40el/3t7pEFNTpc+57bZgGu/C0Gmli3u2CI/yZhKSolBsOfIH2DPUndihZWqFMspJqXnFezmqYNo34p0YspmGXHHFn2aPTJJRxtQME6fc4VMbBbxQO1oY0KnVkoMYr/CtwC1yXnUaPm+/DIrWMlJ9oPDjHhQyW6ehknGtyLTJXff0UZV86Obktxo1ngMTWzmn78w8oFaIqIkBsFRAMjNZKl2DddLL5PvLiq3gtUw0R4cwqXTtyGV10unBM9unsZJxuA30yV3bPh5qiNInZ5uIDdfatcfmwW0t8quKqWGeNoDQa9upKNGQ/j27KiJwZrnhOyjYbXJXWm+HzXzAEX7ivytdequr0UaPKhU+83BzN08UyoJ34rMl9yN7IuezkIWnwYgvVGWrwF++yttfdsDOk8F575JlPDt2VFHuUoS+16QSE0o2Q8Ok329WAuZp+s3BzML/VZk6/Ni0IDeMuZL7iNRXoHUlz1UR5s0AOma6+KbeqCrHehV2e/eZgtfaSqU062qNiIO9MtvOKvy4XYCNaFkzw+TzOvJNgEd+iTymRS7OCZd4FuR0+VCZ6f8egYJnV/3M1JyXftdYHyR7CbxtEdKblEW0ojq3NnYx+Y4gGnXK29XOV2DVaGnj9qEF7Z4yNXTIcwqle3tIyvZC30k83pyTUBRpoom8zCk5n7o0CFs3boVfr8ft912GxYsWGDEZeRl56qvcZpBtIfHzY0Qf7ossfOPirHgt7cHaDqgvL27E2L1E/A/+svwlZc+qQde3ig1owkCfAXjAWmKs4vHjh4LsWA8fP9rwcV57QvGSQ+Ov2mRvi1ccgmw6GFYZ5VCPNEMHPwYuHABoigC+/8Mn88PWC3AoE+a4yZk/7BJz4oul/47OyDVrKeXQKx+AqcG+oGxdmDxCmlZRhmKi4colCfzQaWWhK1lYRRKnO+Dt4E3f4dTfr/UEeLuJbDe/gPdzi+Ior4zYfn9fqxYsQJPPPEECgoKsHr1aqxYsQITJ06Melxrq/qZA33/U78XgJJkqGZtcRdKiX1Ltb7nn3MHUPeO+v3LlwL/9w8RzThC5VppVGvNmvDRvxYrULk2IsHLTp7mLgQWLQ9r1w49v17J0aXi67yv+gng6GfqTrj0UVhnlQZ/VLq3WPegJq5USKe4fB+8HT7JX0D5Uk0JvqhI/ls7YECzzFdffYXCwkKMHz8eNpsNN9xwAxoaGvS+DGWa0AEaL2/U//xaEjsAvPk75R4r256LnNbB75Mf7arU82Xbc4YPUlGlTX5aB1k7t4f/nISBNiPWm7/TVh4H3ZtlPB4PCgoKgj8XFBTgyy+/jNivtrYWtbW1AICqqiq4NPQnTrPZYkglW58XTpcLp/Se+TIeCssX2vq8uKD0cHegP+J96unzyq79CoVzBF4DPdhstpifm1NaejwNuz+le4t1D2riSoV0iuuU0vKZfr9uMaast0xZWRnKysqCP6fL1yUyzmBWjvR7tl0Sd/973Vgssgl+MCtHamPv7408Zqw94n3qz1KYNkHhHMHXQAeqmhmU7kVh39DzKd1brHtIp+aPUGkVl8L7DxaLphiT2izjdDrR1XWxW15XVxecziTORWFhB6C0FNobZNHD+p9/zh3a9r97iXKPlcUrpDb2UBarVD6cUs+XxSuS2wNHidy9CDKfEbn7S3YvopHk7iXayuNgffLJJ5/U7WwA8vLy8MYbb6CkpASjR4/Gtm3b8MMf/hAOhyPqcV6v+hkGLT+4B+Lv/zOi3Pq/34Y4ZRrwxWH1/aMpujl3AH+NbFYLY7tEmsPFYgV8keNMhVmlEBavCD6Es0y8AuL4IuDIAan2YrFI0wppTGUAAAhCSURBVATYc8LntL+jHPj2fwG+OHSxS2XBOODSidI6sqIIjBoF/OtKWP/b3SHnHNrXZpM639isUplgubj/Lf8VmDETQu8ZIDsXwpXfCsZocY2X3kfHjkg9bHLzgAdXy/aWEbKyZc9j/afJiufXi91uR3+/QhPSkLB7AaSeRg+uBm64LaJs+P0p3Vuse1ATVyqkU1yWyVdDHJt18b1tsQD//X9o7i2Tk6PwzREG9JYBgAMHDuCll16C3+/HrbfeirvuuivmMVp6y4RKq69aIRiXNoxLu3SNjXFpk0hc0ZplDGlzv/7663H99VEGthARkaHYQE1EZEJM7kREJsTkTkRkQkzuREQmZEhvGSIiSq2Mr7mvWrUq1SHIYlzaMC7t0jU2xqWNUXFlfHInIqJITO5ERCak+/QDqVBcXJzqEGQxLm0Yl3bpGhvj0saIuPhAlYjIhNgsQ0RkQkzuREQmlLLFOrSKtej2hQsXsHHjRpw4cQI5OTlYuXIlxo0bZ2hMnZ2d2LRpE06fPg1BEFBWVoY77gifV7ypqQm/+tWvgrHMmjULd999t6FxAcBDDz2EMWPGwGKxwGq1oqqqKmy7KIrYunUrDh48iNGjR6OiosLw9sjW1lbU1NQEf25vb0d5eTnuvPPOYFkyX6/NmzfjwIEDcDgcqK6W1nTt7e1FTU0NOjo64Ha7UVlZiezs7Ihj6+rq8NZbbwEA7rrrLsyZM8ewmLZv3479+/fDZrNh/PjxqKioQFZWVsSxsX7nRsT2+uuv409/+hNyc3MBAPfcc4/spIGxPr96x1VTUxOcaba/vx92ux1PP/10xLFGvWZKuSGp7y8xA/h8PvHhhx8W29raxAsXLog/+clPxG+++SZsn3fffVd84YUXRFEUxQ8//FB89tlnDY/L4/GIx48fF0VRFPv7+8VHHnkkIq4jR46I69atMzyW4SoqKsSenh7F7fv37xefeuop0e/3i83NzeLq1auTGJ30O126dKnY3t4eVp7M16upqUk8fvy4+OMf/zhYtn37dnHnzp2iKIrizp07xe3bt0cc5/V6xYceekj0er1h/zYqpkOHDomDg4PB+ORiEsXYv3MjYtuxY4e4e/fuqMep+fzqHVeol156SXzjjTdktxn1minlhmS+vzKiWUbNotv79u0L/nWbPXs2jhw5AtHgZ8X5+fnB2u7YsWMxYcIEeDweQ6+pl3379uGWW26BIAi46qqr0NfXh+7u7qRdv7GxEYWFhXC73Um75nDXXHNNRK2poaEBpaWlAIDS0lLZxd0PHTqEGTNmIDs7G9nZ2ZgxYwYOHTpkWEzXXnstrFZpNaWrrroqZe8xudjUUPP5NSouURTxl7/8BTfeeKNu11NDKTck8/2VEc0yahbdDt3HarXCbrfD6/UGvy4arb29HS0tLbjyyisjth07dgyPPfYY8vPzcf/99+Oyyy5LSkxPPfUUAOD2228PW68WkF6v0IV4CwoK4PF4kJ+fn5TY/vznPyt+4FL1egFAT09P8DXIy8tDT09PxD7D349OpzNpCXfPnj244YYbFLdH+50b5b333sPevXtRXFyMRYsWRSRaNZ9fo3zxxRdwOBy49NJLFfcx+jULzQ3JfH9lRHJPd2fPnkV1dTUWL14Mu90etm3SpEnYvHkzxowZgwMHDuDpp5/Ghg0bDI/pF7/4BZxOJ3p6evDLX/4SRUVFuOaaawy/rhqDg4PYv38/7r333ohtqXq95AiCAEEQUnJtOW+99RasVituvvlm2e2p+J3Pmzcv+Exkx44dePnll1FRUWHoNbWIVokAjH/NouUGo99fGdEso2bR7dB9fD4f+vv7o64vqJfBwUFUV1fj5ptvxqxZsyK22+12jBkzBoC0QpXP58OZM2ci9tNb4PVxOByYOXMmvvrqq4jtoUt7JXMh84MHD2LSpEnIy8uL2Jaq1yvA4XAEm6e6u7tlv/kNfz96PB7DX7u6ujrs378fjzzyiGJCiPU7N0JeXh4sFgssFgtuu+02HD9+XDauWJ9fI/h8Pnz66adRv+kY+ZrJ5YZkvr8yIrlPnjwZJ0+eRHt7OwYHB/HRRx+hpKQkbJ/vfOc7qKurAwB8/PHHmDZtmuG1LlEU8fzzz2PChAn43ve+J7vP6dOng23/X331Ffx+v+F/dM6ePYuBgYHgvz/77DNcfvnlYfuUlJRg7969EEURx44dg91uT4smmVS8XqFKSkpQX18PAKivr8fMmTMj9rnuuutw+PBh9Pb2ore3F4cPH8Z1111nWEyHDh3C7t278fjjj2P06NGy+6j5nRsh9DnNp59+KtuEpubza4TGxkYUFRWFNXGEMvI1U8oNyXx/ZcwIVblFt3fs2IHJkyejpKQE58+fx8aNG9HS0oLs7GysXLkS48ePNzSmo0ePYs2aNbj88suDf0juueeeYI143rx5ePfdd/H+++/DarVi1KhRWLRoEa6++mpD4zp16hSeeeYZAFLt5aabbsJdd92F999/PxiXKIp48cUXcfjwYYwaNQoVFRWYPHmyoXEB0oeooqICGzduDH5NDY0rma/X+vXr8fnnn8Pr9cLhcKC8vBwzZ85ETU0NOjs7w7qqHT9+HB988AEeeOABAFLb986dOwFIXdVuvfVWw2LauXMnBgcHg23ZU6ZMwbJly+DxePDCCy9g9erVir9zPcnF1tTUhL/+9a8QBAFutxvLli1Dfn5+WGyA/OfXyLjmzp2LTZs2YcqUKZg3b15w32S9Zkq5YcqUKUl7f2VMciciIvUyolmGiIi0YXInIjIhJnciIhNiciciMiEmdyIiE2JyJyIyISZ3IiIT+v+NajTs8dX02gAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "-QCkBUy7EfAk",
        "outputId": "9cc7e9a3-dcd1-48de-b5b1-29222a28f0bd"
      },
      "source": [
        "neg_corr = postDB.loc[postDB['c_rating']=='negativo']\r\n",
        "neg_corr\r\n",
        "\r\n",
        "correlation_coeff_4 = np.corrcoef(neg_corr[\"p_Emo_Neg\"], neg_corr[\"c_Emo_Neg\"])\r\n",
        "display(correlation_coeff_4)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(neg_corr[\"p_Emo_Neg\"], neg_corr[\"c_Emo_Neg\"])\r\n",
        "plt.show()"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.07183618],\n",
              "       [0.07183618, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "PMqVDA8VF4Ng",
        "outputId": "96bc79a7-b7e3-4d18-f06a-8158e9372ee0"
      },
      "source": [
        "pos_corr = postDB.loc[postDB['c_rating']=='positivo']\r\n",
        "pos_corr\r\n",
        "\r\n",
        "correlation_coeff_4 = np.corrcoef(pos_corr[\"p_Emo_Neg\"], pos_corr[\"c_Emo_Neg\"])\r\n",
        "display(correlation_coeff_4)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(pos_corr[\"p_Emo_Neg\"], pos_corr[\"c_Emo_Neg\"])\r\n",
        "plt.show()"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.06532251],\n",
              "       [0.06532251, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mKYB0hmuMG4O"
      },
      "source": [
        "## Positive Emotions"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "YzfEjexyJG3G",
        "outputId": "58ab85b0-aa80-4319-9697-7421fc93db3d"
      },
      "source": [
        "#No rating, general\r\n",
        "correlation_coeff_5 = np.corrcoef(df_post[\"c_Emo_Pos\"] , df_post[\"c_Emo_Pos\"] )\r\n",
        "display(correlation_coeff)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(hate_posts, hate_comments)\r\n",
        "plt.show()\r\n",
        "\r\n",
        "\r\n",
        "#Hate rating\r\n",
        "hate_corr = postDB.loc[postDB['c_rating']=='hate']\r\n",
        "hate_corr\r\n",
        "\r\n",
        "correlation_coeff_6 = np.corrcoef(hate_corr[\"p_Emo_Pos\"], hate_corr[\"c_Emo_Pos\"])\r\n",
        "display(correlation_coeff_6)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(hate_corr[\"p_Emo_Pos\"], hate_corr[\"c_Emo_Pos\"])\r\n",
        "plt.show()\r\n",
        "\r\n",
        "#Negative Rating\r\n",
        "neg_corr = postDB.loc[postDB['c_rating']=='negativo']\r\n",
        "neg_corr\r\n",
        "\r\n",
        "correlation_coeff_7 = np.corrcoef(neg_corr[\"p_Emo_Pos\"], neg_corr[\"c_Emo_Pos\"])\r\n",
        "display(correlation_coeff_7)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(neg_corr[\"p_Emo_Pos\"], neg_corr[\"c_Emo_Pos\"])\r\n",
        "plt.show()\r\n",
        "\r\n",
        "#Positive rating\r\n",
        "pos_corr = postDB.loc[postDB['c_rating']=='positivo']\r\n",
        "pos_corr\r\n",
        "\r\n",
        "correlation_coeff_8 = np.corrcoef(pos_corr[\"p_Emo_Pos\"], pos_corr[\"c_Emo_Pos\"])\r\n",
        "display(correlation_coeff_8)\r\n",
        "\r\n",
        "plt.style.use('ggplot')\r\n",
        "\r\n",
        "plt.scatter(pos_corr[\"p_Emo_Pos\"], pos_corr[\"c_Emo_Pos\"])\r\n",
        "plt.show()"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.05976614],\n",
              "       [0.05976614, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3dfXAc9Z3n8XfPjJ8kWQ8jyVZs4wVhE8dewRZnn52sWRFQnDoga3aPdYozYV2cN3U4OF7F3AU2rOM1EFQbFAlYU2wWyg7gu5CrHPbeHrukFApvkRSJWPPgtWPHGIcQjKyHkWQ9+UEzfX+0JUua7pme0WhmuvV5VaWCevrhq7b9VevX39/3Z5imaSIiIr4SyHUAIiKSeUruIiI+pOQuIuJDSu4iIj6k5C4i4kNK7iIiPhTKdQAjTp8+ndZxFRUVdHZ2Zjiaqae4s8eLMYPiziYvxgywYMECx8/05C4i4kNK7iIiPqTkLiLiQ0ruIiI+pOQuIuJDSatlnn76aQ4dOkRJSQmNjY0A9Pf309TUREdHB5WVldTX11NUVIRpmuzZs4e3336bWbNmsWXLFqqrq6ck8Ohj/wM+OMaZkQ3Vywg++LcAxDra4MA+zN9+AGc+hljM2icYgtIwbNqGUV5p7dMTgdlzoO8s/Pakte/sOXBuCEwTDOPy14EALPkMxt33Wee7dLxRGob1GwlUVjnGOxrTpet1z5xF9GxPwmPHHmOUhjHXrsN44yeOX4+cZ+JxyWITEf8xknWFPHr0KLNnz2b37t2jyf3FF1+kqKiI22+/nf3799Pf389dd93FoUOH+Jd/+RcefPBBTpw4wd69e/nOd77jKpBUSiFHEnuc6mUYm7+B2bQDOtoSnMGAkjLojbi+5jiFc2HWbIh0XN5WWYVRv8sxSSeMyeZY22MCQYhFnb+urIK7t8LzT40/LkFsqfJiyZgXYwbFnU1ejBkmWQq5fPlyioqKxm1rbW2ltrYWgNraWlpbWwF46623+KM/+iMMw+Caa65hYGCA7u7uycRuzy6xj2w/sC9JYgcw00/sAAN94xM7WNc8sM9+/2Qx2R1rd8zYRG73dUcb7H0i/rhEsYmIL6U1iam3t5eysjIASktL6e3tBSASiVBRUTG6X3l5OZFIZHTfsVpaWmhpaQGgoaFh3HHJnEnwWWigj4uuz5RZoYE+wjbfR8RFTBOPdXOMraHBlGJLVSgUSunPKh94MWZQ3NnkxZiTmfQMVcMwMAwj5ePq6uqoq6sb/TpTvxINF87NyHnSvbbd9xFzEdPEY90cY2tOAQz2u44tVV789dWLMYPiziYvxgxTMEO1pKRkdLilu7ub4uJiAMLh8Lgb1NXVRTgcTucSiVUvc96+fqM19pyQASWTiKtwLoQrx2+rrLKubSdZTHbH2h0TCCb+urIKNm2LPy5RbCLiS8GdO3fuTLbTwMAAP/vZz/jiF78IWE/Zn3zyCcuWLePVV1+lsrKSa6+9FsMw+OlPf8ratWs5ceIER44c4bbbbnMVSF9fn+ugAzd8AfPI29A95iftpWoZo7AIrl2F0X/WqnwZ7LeqXsCqlglXwJa/wvjCemufomJYdKWVsPt6AQPmFEI0av13IHD562AIrvl9jK1/jfG5m0ePN5Z8BmPTNscXluNiunS9mYuric4tcTx24jHGks/AlzdjxKKOXxubthH8vavjjksUW6oKCgoYHLQf+slXXowZFHc2eTFmgLlznX/DT1ot09zczNGjR+nr66OkpIQNGzawatUqmpqa6OzsjCuFfO6553j33XeZOXMmW7Zs4eqrr3YVpBqHeYMX4/ZizKC4s8mLMUPiYZmkyT1blNy9wYtxezFmUNzZ5MWYQV0hRUSmHSV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxISV3EREfUnIXEfEhJXcRER9SchcR8SEldxERH1JyFxHxodBkDv6nf/onXnvtNQzD4IorrmDLli309PTQ3NxMX18f1dXVbN26lVBoUpcREZEUpf3kHolE+Od//mcaGhpobGwkFovx85//nBdffJFbb72Vp556isLCQl577bVMxisiIi5MalgmFotx4cIFotEoFy5coLS0lCNHjrBmzRoAbrzxRlpbWzMSqIiIuJf2eEk4HOZLX/oS9957LzNnzuS6666jurqagoICgsHg6D6RSMT2+JaWFlpaWgBoaGigoqIirThCoVDax+aS4s4eL8YMijubvBhzMmkn9/7+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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[ 1.        , -0.15606321],\n",
              "       [-0.15606321,  1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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Q2Ipr6Wskq28lrJKtvJayirFPy//iQkARjGFAgBGUeAAYFTCF3SIRqTFkXt6evTSSy/p9OnTSk1NVUVFhW655RZJ0s6dO1VXVye3260nnnhCs2bNSmrWP/zhD9q7d688Ho/S0tL0/e9/X9nZ2ZKkb3/728rPz5d05cvof/SjHyU0azR59+/fr9/85jfh73J/8MEHVVpaGn7vjTfekCQtWrRI8+bNS2rW1157TcePH5ckXb58WR0dHXrttdckjfy5rampUWNjo9LT01VVVTXgfcdx9Oqrr+qvf/2rbrrpJpWXl4fnP0f6vEaT9+2339bu3bvlOI7Gjx+vFStW6Mtf/rIkaeXKlRo3bpzcbrc8Ho8qKyuTmvX48eP6+c9/Hu6A4uJifetb35I0MgutDyXr73//e7399tuSrqwj/O9//1vbt2+X1+uNz3l1kqyvr89ZtWqVc/78eaenp8d5+umnnQ8//LDfNm+99Zbz8ssvO47jOH/+85+dX/ziF47jOM6HH37oPP30087ly5edCxcuOKtWrXL6+vqSmvVvf/ub093d7TiO4+zZsyec1XEcZ+nSpQnLFmveffv2Oa+88sqAfTs7O52VK1c6nZ2d/X5OZtZrvfnmm051dXX49Uif2+PHjzunTp1yfvCDHwz6/nvvveds2rTJCYVCTnNzs/Pss886jjPy5zXavO+//344R2NjYziv4zhOeXm509HRkfCMV0XKeuzYMeenP/3pgPGh/h0aiazXamhocDZs2BB+HY/zmvQplGgWRz58+HD4KuWuu+7SsWPH5DiOGhoadPfdd2vMmDG65ZZblJOTo5MnTyY16/Tp03XTTTdJkqZNm6ZAIJCwPJEMZ+HppqYmzZw5U16vV16vVzNnzlRTU9OoyXrw4EHNnTs3YXkiKSwslNfrve77hw8f1je+8Q25XC7ddtttunjxooLB4Iif12jz3n777eH3p02b1m+1rZEWKev1jMhC658zlKwHDx7UPffcE9fjJ30KJZrFka/dxuPxaMKECers7FQgENC0adPC22VlZSW0MKNdyPmqurq6flM6PT09Wrt2rTwejx555BF9/etfT1jWoeR955139Pe//11f+tKX9J3vfEc+n2/AvqPp3La2tqqlpUXTp08Pj430uY0kEAj0W3B34sSJCgQCI35eY1FXV6evfe1r/cY2bdokSXrggQf6rXGbLB988IHWrFmjzMxMLVu2TJMnTx7yv8+R9N///ldNTU363ve+1298uOc16QX+/1V9fb1Onz6ta2+zr6mpUVZWli5cuKCNGzcqPz9fOTnxWVopVnfeeafuuecejRkzRn/6059UXV2t9evXJzVTJAcPHtRdd90lt/uzD5Cj8dxadOzYMe3bt08bN24Mjz333HPKyspSR0eHnn/+eeXm5qqwsDBpGb/yla+opqZG48aNU2Njo1544QW9+OKLScsTjffee6/fpxwpPuc16VMo0SyOfO02fX19+vTTT5Wamjpg30AgEP+FlYeYVZKOHj2qnTt36plnntGYMWP67S9JkyZNUmFhoc6ePZuwrNHmTU1NDWcsLS3V6dOnB913tJxbSTp06NCAj6IjfW4jycrK6rd81tU/z0if16H45z//qZdffllr1qxRaupnq6lfzZeenq45c+YkdJoyGhMmTNC4ceMkXVkVrK+vT5988snILLQeo8Gm/OJxXpNe4NEsjnznnXdq//79kqS//OUv+upXvyqXy6WioiIdOnRIPT09amlp0UcffaSpU6cmNeuZM2f0q1/9Ss8884zS09PD411dXerp6ZEkffLJJ2pubtatt96asKzR5g0Gg+GfDx8+HM40a9YsHTlyRF1dXerq6tKRI0cSeodPtItk/+c//9HFixd12223hceScW4jKSoqUn19vRzH0QcffKAJEyYoMzNzxM9rtNra2rR582atWrVKubm54fHu7m5dunQp/PPRo0fDd/skS3t7u5z/PX948uRJhUIhpaamjshC67H49NNPdeLEiX5Z4nVeR8WTmI2Njfr1r38dXhx50aJF2rFjh6ZMmaKioiJdvnxZL730ks6cOSOv16uKigpNmjRJkvTGG29o3759crvdevzxxwfM3Y101ueee07/+te/lJGRIemzW9qam5v1y1/+Um63W6FQSAsWLND999+f0KzR5P3d736nw4cPy+PxyOv1asWKFcrLy5N0ZS50586dkq7c7nbfffclNask1dbWqqenR4899lh4v2Sc261bt+rEiRPq7OxUenq6Fi9erN7eXknSN7/5TTmOo+3bt+vIkSMaO3asysvLNWXKFEkjf16jybtt2za988474Xn7q7e1XbhwQZs3b5Z05dPv3LlztWjRoqRmfeutt/THP/5RHo9HY8eO1fLly3X77bdLGvzvUDKzSlduG21qalJFRUV4v3id11FR4ACAoUv6FAoAIDYUOAAYRYEDgFEUOAAYRYEDgFEUOAAYRYEDgFH/B58xrHbWKS2RAAAAAElFTkSuQmCC\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.03470038],\n",
              "       [0.03470038, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "array([[1.        , 0.04176635],\n",
              "       [0.04176635, 1.        ]])"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    }
  ]
}