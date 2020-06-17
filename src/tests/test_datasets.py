from cmdc_tools import datasets
import pytest
import pandas as pd


nodates = datasets.DatasetBaseNoDate.__subclasses__()
yesdates = datasets.DatasetBaseNeedsDate.__subclasses__()
all_ds = nodates + yesdates


@pytest.mark.parametrize("cls", nodates)
def test_no_date_datasets(cls):
    if cls is datasets.WEI:
        print("Skipping!")
        assert True
        return
    d = cls()
    out = d.get()
    assert isinstance(out, pd.DataFrame)
    assert out.shape[0] > 0


@pytest.mark.parametrize("cls", yesdates)
def test_need_date_datasets(cls):
    d = cls()
    out = d.get("2020-05-25")
    assert isinstance(out, pd.DataFrame)
    assert out.shape[0] > 0


@pytest.mark.parametrize("cls", all_ds)
def test_all_dataset_has_type(cls):
    assert hasattr(cls, "data_type")


@pytest.mark.parametrize("cls", all_ds)
def test_covid_dataset_has_source(cls):
    if getattr(cls, "data_type", False) == "covid":
        assert hasattr(cls, "source")
